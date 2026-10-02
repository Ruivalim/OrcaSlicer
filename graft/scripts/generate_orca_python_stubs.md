# scripts/generate_orca_python_stubs.py

- log · function · L30-L31 — def log(message: str) -> None
- run · function · L34-L36 — def run(command: list[str], *, env: dict[str, str] | None = None, cwd: Path = REPO_ROOT) -> None
- venv_python · function · L39-L42 — def venv_python(venv_dir: Path) -> Path
- ensure_venv · function · L45-L50 — def ensure_venv(venv_dir: Path) -> Path
- ensure_stubgen · function · L53-L63 — def ensure_stubgen(python: Path) -> None
- module_suffixes · function · L66-L71 — def module_suffixes() -> list[str]
- is_orca_extension · function · L74-L79 — def is_orca_extension(path: Path) -> bool
- find_module_dir · function · L82-L104 — def find_module_dir(build_dir: Path, config: str) -> Path | None
- build_stubgen_module · function · L107-L117 — def build_stubgen_module(build_dir: Path, config: str) -> None
- import_env · function · L120-L127 — def import_env(module_dir: Path) -> dict[str, str]
- verify_import · function · L130-L136 — def verify_import(python: Path, module_dir: Path) -> None
- clean_output · function · L139-L145 — def clean_output(output_dir: Path) -> None
- generate_stubs · function · L148-L152 — def generate_stubs(python: Path, module_dir: Path, output_dir: Path, ignore_errors: bool) -> None
- parse_args · function · L155-L169 — def parse_args() -> argparse.Namespace
- main · function · L172-L208 — def main() -> int
