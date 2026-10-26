"""Synchronize static presentation artifacts and export the public file allowlist."""

import argparse
import hashlib
import html
import json
from pathlib import Path
import re
import shutil


ROOT = Path(__file__).resolve().parent.parent
METRICS = ("accuracy", "precision", "recall", "f1")
ISLAND = re.compile(
    r'(<script type="application/hyperframes-slideshow\+json">)(.*?)(</script>)',
    re.DOTALL,
)
PUBLIC_FILES = (
    "index.html", "slides.html", "README.md", "tools/prepare.py",
    "assets/aihub-child-counseling.png",
    "assets/aihub-child-counseling.source.json",
    "assets/local-model-results.source.json", "assets/share-preview.png",
    "assets/vendor/gsap.min.js", "assets/vendor/hyperframes-player.global.js",
    "assets/vendor/hyperframes-slideshow.global.js",
    "assets/vendor/HYPERFRAMES-LICENSE",
)


def replace_one(pattern: str, replacement: str, text: str) -> str:
    """Fail on missing or duplicated generated regions."""
    result, count = re.subn(pattern, lambda _: replacement, text, flags=re.DOTALL)
    if count != 1:
        raise ValueError(f"Expected one generated region, found {count}: {pattern}")
    return result


def result_rows(source: dict, target: str) -> str:
    models = {**source["models"], **source["api_models"]}

    def value(model: dict, metric: str) -> float:
        stored = model["targets"][target][metric]
        return stored["mean"] if isinstance(stored, dict) else stored

    rows = []
    for rank, key in enumerate(sorted(
        models, key=lambda key: value(models[key], "f1"), reverse=True
    )):
        model = models[key]
        marker = (
            '<sup class="result-once">*</sup>'
            if model.get("display_aggregation") == "1회차" else ""
        )
        style = ' class="result-best"' if rank == 0 else ""
        cells = "".join(f"<td>{value(model, metric) * 100:.2f}</td>" for metric in METRICS)
        rows.append(
            f'<tr data-model="{html.escape(key)}"{style}>'
            f'<th scope="row">{html.escape(model["name"])}{marker}</th>{cells}</tr>'
        )
    return "<tbody>" + "".join(rows) + "</tbody>"


def synchronize() -> dict[str, str]:
    source = json.loads((ROOT / "assets/local-model-results.source.json").read_text())
    slides = (ROOT / "slides.html").read_text()
    for target in ("suicide", "self_harm", "stage"):
        pattern = rf'<section id="results_{target}".*?</section>'
        section = re.search(pattern, slides, re.DOTALL).group()
        section = replace_one(r"<tbody>.*?</tbody>", result_rows(source, target), section)
        slides = replace_one(pattern, section, slides)

    # HyperFrames requires a static island in both files; edit only the composition.
    metadata = json.loads(ISLAND.search(slides)[2])
    ids = re.findall(r'<section[^>]*data-composition-id="([^"]+)"', slides)
    if ids != [slide["sceneId"] for slide in metadata["slides"]]:
        raise ValueError("Scene order and slideshow metadata disagree")
    island = ISLAND.search(slides).group()
    index = ISLAND.sub(lambda _: island, (ROOT / "index.html").read_text())
    digest = hashlib.sha256(slides.encode()).hexdigest()[:12]
    index = replace_one(r'src="slides.html\?v=[^"]+"', f'src="slides.html?v={digest}"', index)
    return {"slides.html": slides, "index.html": index}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check without writing")
    parser.add_argument("--export", type=Path, help="Copy only public presentation files")
    args = parser.parse_args()
    if args.check and args.export:
        parser.error("--check and --export cannot be combined")
    generated = synchronize()
    changed = [name for name, text in generated.items() if (ROOT / name).read_text() != text]
    if args.check:
        if changed:
            raise SystemExit("Out of sync: " + ", ".join(changed))
        print("Presentation tables, metadata, and asset version are in sync.")
        return
    for name in changed:
        (ROOT / name).write_text(generated[name])
    if args.export:
        destination = args.export.resolve()
        if destination == ROOT or ROOT.is_relative_to(destination):
            parser.error("Export destination must not contain the source presentation")
        for name in PUBLIC_FILES:
            target = destination / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / name, target)
        print(f"Exported {len(PUBLIC_FILES)} public files to {destination}")
    else:
        print("Updated: " + (", ".join(changed) or "already in sync"))


if __name__ == "__main__":
    main()
