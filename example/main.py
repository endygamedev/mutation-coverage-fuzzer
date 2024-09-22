from mutation_coverage_fuzzer.runner import Runner

from cgi_decoder import cgi_decode


def main() -> None:
    # cgi_decode("+")
    # cgi_decode("%20")
    # cgi_decode("abc")

    runner = Runner(cgi_decode)

    runner.run("+")
    covered_lines = len(runner.coverage_tracker.covered_lines)
    lines = len(runner.coverage_tracker.lines)
    print(f"{covered_lines}/{lines}")

    runner.run("%20")
    covered_lines = len(runner.coverage_tracker.covered_lines)
    lines = len(runner.coverage_tracker.lines)
    print(f"{covered_lines}/{lines}")

    runner.run("abc")
    covered_lines = len(runner.coverage_tracker.covered_lines)
    lines = len(runner.coverage_tracker.lines)
    print(f"{covered_lines}/{lines}")


if __name__ == "__main__":
    main()
