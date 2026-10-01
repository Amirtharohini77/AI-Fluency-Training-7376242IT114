"""Day 4 assessment: model memory estimator."""


BYTES_PER_PARAM = {
    "FP16": 2.00,
    "Q8_0": 1.00,
    "Q6_K": 0.81,
    "Q5_K_M": 0.68,
    "Q4_K_M": 0.57,
    "Q3_K_M": 0.43,
}


KV_GB_PER_B_PER_1K = 0.02
OVERHEAD = 1.10


def estimate(params_b, precision, context_k):
    if precision not in BYTES_PER_PARAM:
        raise ValueError(
            f"Unknown precision: {precision}"
        )

    weights = params_b * BYTES_PER_PARAM[precision]

    kv_cache = (
        params_b
        * context_k
        * KV_GB_PER_B_PER_1K
    )

    total = (
        weights + kv_cache
    ) * OVERHEAD

    return weights, kv_cache, total


def verdict(total_gb, available_gb):

    if total_gb <= available_gb * 0.7:
        return "fits comfortably"

    if total_gb <= available_gb:
        return "fits, but tight"

    return "does NOT fit"


def report(
    name,
    params_b,
    precision,
    context_k,
    available_gb
):

    weights, kv, total = estimate(
        params_b,
        precision,
        context_k
    )

    print(
        f"{name:<20} "
        f"{params_b:>5.1f}B "
        f"{precision:<7} "
        f"{context_k:>4}K "
        f"weights={weights:>6.2f}GB "
        f"KV={kv:>5.2f}GB "
        f"total={total:>6.2f}GB "
        f"-> {verdict(total, available_gb)}"
    )


if __name__ == "__main__":

    AVAILABLE_GB = 16.0  # CHANGE TO YOUR REAL VALUE

    print(
        f"Available memory: {AVAILABLE_GB} GB\n"
    )

    # At least four configurations
    report(
        "Qwen small",
        1.5,
        "Q4_K_M",
        8,
        AVAILABLE_GB
    )

    report(
        "8B Q4",
        8.0,
        "Q4_K_M",
        8,
        AVAILABLE_GB
    )

    report(
        "8B FP16",
        8.0,
        "FP16",
        8,
        AVAILABLE_GB
    )

    report(
        "14B Q4",
        14.0,
        "Q4_K_M",
        8,
        AVAILABLE_GB
    )


    print(
        "\nContext experiment: 8B Q4"
    )

    for context in (
        4,
        8,
        16,
        32
    ):

        report(
            "8B Q4",
            8.0,
            "Q4_K_M",
            context,
            AVAILABLE_GB
        )


    print(
        "\nQuantization experiment: 8B at 8K"
    )

    for precision in (
        "Q3_K_M",
        "Q4_K_M",
        "Q5_K_M",
        "Q8_0",
        "FP16"
    ):

        report(
            "8B",
            8.0,
            precision,
            8,
            AVAILABLE_GB
        )