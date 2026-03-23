from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


NumericValue = Union[int, float]


class DataValidationError(Exception):
    def __init__(self, processor_name: str, message: str) -> None:
        super().__init__(f"{processor_name}: {message}")


class DataProcessor(ABC):
    def __init__(self, processor_name: str) -> None:
        self.processor_name = processor_name

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Numeric Processor")

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list) or len(data) == 0:
            return False
        return all(isinstance(value, (int, float)) for value in data)

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise DataValidationError(
                    self.processor_name,
                    "expected a non-empty list of numeric values",
                )

            numeric_data: List[NumericValue] = data
            total: NumericValue = sum(numeric_data)
            average: float = total / len(numeric_data)
            result = (
                f"Processed {len(numeric_data)} numeric values, "
                f"sum={total}, avg={average:.1f}"
            )
            return self.format_output(result)
        except TypeError as exc:
            raise DataValidationError(
                self.processor_name,
                "numeric calculation failed",
            ) from exc


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Text Processor")

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and len(data.strip()) > 0

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise DataValidationError(
                    self.processor_name,
                    "expected a non-empty text string",
                )

            text_data: str = data.strip()
            word_count: int = len(text_data.split())
            result = (
                f"Processed text: {len(text_data)} characters, "
                f"{word_count} words"
            )
            return self.format_output(result)
        except AttributeError as exc:
            raise DataValidationError(
                self.processor_name,
                "text processing failed",
            ) from exc


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Log Processor")

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str) or ":" not in data:
            return False
        level, message = data.split(":", 1)
        return len(level.strip()) > 0 and len(message.strip()) > 0

    def _parse_log_entry(self, data: str) -> Dict[str, Optional[str]]:
        level, message = data.split(":", 1)
        parsed_log: Dict[str, Optional[str]] = {
            "level": level.strip().upper(),
            "message": message.strip(),
        }
        return parsed_log

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise DataValidationError(
                    self.processor_name,
                    "expected log text in the format LEVEL: message",
                )

            log_data: str = data
            parsed_log = self._parse_log_entry(log_data)
            level: str = parsed_log["level"] or "UNKNOWN"
            message: str = parsed_log["message"] or "No message provided"
            result = f"[{level}] {level} level detected: {message}"
            return self.format_output(result)
        except ValueError as exc:
            raise DataValidationError(
                self.processor_name,
                "log parsing failed",
            ) from exc

    def format_output(self, result: str) -> str:
        if result.startswith("[ERROR] ERROR"):
            return result.replace(
                "[ERROR] ERROR level detected",
                "[ALERT] ERROR level detected",
                1,
            )
        return result


def display_data(data: Any) -> str:
    if isinstance(data, str):
        return f'"{data}"'
    return str(data)


def validation_message(processor: DataProcessor, is_valid: bool) -> str:
    if not is_valid:
        return "Validation: failed"
    if isinstance(processor, NumericProcessor):
        return "Validation: Numeric data verified"
    if isinstance(processor, TextProcessor):
        return "Validation: Text data verified"
    return "Validation: Log entry verified"


def run_demo(processor: DataProcessor, data: Any) -> None:
    print(f"Initializing {processor.processor_name}...")
    print(f"Processing data: {display_data(data)}")
    try:
        is_valid: bool = processor.validate(data)
        print(validation_message(processor, is_valid))
        print(f"Output: {processor.process(data)}")
    except DataValidationError as exc:
        print(f"Output error: {exc}")
    print()


def polymorphic_process(
    processors: List[DataProcessor],
    data_stream: List[Any],
) -> None:
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    for index, (processor, data) in enumerate(zip(processors, data_stream),
                                              start=1):
        try:
            result = processor.process(data)
            print(f"Result {index}: {result}")
        except DataValidationError as exc:
            print(f"Result {index}: {exc}")


def main() -> None:
    numeric_processor = NumericProcessor()
    text_processor = TextProcessor()
    log_processor = LogProcessor()

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    run_demo(numeric_processor, [1, 2, 3, 4, 5])
    run_demo(text_processor, "Hello Nexus World")
    run_demo(log_processor, "ERROR: Connection timeout")

    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]
    data_stream: List[Any] = [
        [1, 2, 3],
        "Hello Matrix",
        "INFO: System ready",
    ]
    polymorphic_process(processors, data_stream)

    print()
    print("=== Error Handling Demo ===")
    invalid_inputs: List[Any] = ["not a number list", "   ", "BROKEN LOG"]
    for processor, invalid_data in zip(processors, invalid_inputs):
        try:
            processor.process(invalid_data)
        except DataValidationError as exc:
            print(f"Handled error: {exc}")

    print()
    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
