from mutation_coverage_fuzzer.runner import Runner
from mutation_coverage_fuzzer.fuzzer import MutationalCoverageFuzzer

from cgi_decoder import cgi_decode


def main() -> None:
    runner = Runner(cgi_decode)
    seed = {"2%0", "abc+"}
    fuzzer = MutationalCoverageFuzzer(seed, 2, 5, runner, 100_000)
    fuzzer.fuzz()


if __name__ == "__main__":
    main()
