"""Illustrative feature extraction from a generated signal; not production code."""

import math
import statistics


def extract_basic_features(signal: list[float]) -> dict[str, float]:
    if not signal:
        raise ValueError("signal must contain at least one value")
    mean = statistics.fmean(signal)
    return {
        "mean": mean,
        "standard_deviation": statistics.pstdev(signal),
        "root_mean_square": math.sqrt(statistics.fmean(value * value for value in signal)),
        "peak_to_peak": max(signal) - min(signal),
    }


if __name__ == "__main__":
    # Generated mathematical signal; it does not come from a person or device.
    sample_signal = [math.sin(2 * math.pi * index / 32) for index in range(128)]
    for name, value in extract_basic_features(sample_signal).items():
        print(f"{name}: {value:.4f}")
