from typing import Self, Callable, Any
from trace import Trace
from inspect import getsourcelines, getfile


class CoverageTracker:
    def __init__(
        self: Self,
        function: Callable[..., Any],
        *args,
        **kwargs,
    ) -> None:
        self.function = function

        self.lines = set()
        self.covered_lines = set()

    def reset(self: Self) -> None:
        self.lines.clear()
        self.covered_lines.clear()

    def __call__(self: Self, trace: Trace) -> None:
        self.reset()

        source_lines, starting_line_number = getsourcelines(self.function)

        tracer_results = trace.results()
        executed_lines = tracer_results.counts
        module = getfile(self.function)

        function_declaration_offset = 0
        for index, line in enumerate(source_lines):
            if line.strip().endswith(":"):
                function_declaration_offset += index
                break

        start = starting_line_number + function_declaration_offset + 1
        end = len(source_lines) + starting_line_number
        for index in range(start, end):
            self.lines.add(index)
            line_executed = executed_lines.get((module, index), 0) > 0
            if line_executed:
                self.covered_lines.add(index)
