from sympy import *

D1, D2, S1, S2, e, L, c_0, c_L, r_0 = symbols("D1, D2, S1, S2, e, L, c_0, c_L, r_0")
alpha, beta, gamma_1, gamma_2 = symbols("alpha beta gamma_1 gamma_2")

D2 = alpha * D1
S2 = beta * S1
e = gamma_1 * L
r_0 = gamma_2 * L


def print_cartesian_latex():
    a1 = simplify((-D2 * S2 * c_0 + D2 * S2 * c_L) / (D1 * L * S1 + 2 * D2 * S2 * e))
    a2 = simplify((-D1 * S2 * c_0 + D1 * S2 * c_L) / (D1 * L * S1 + 2 * D2 * S2 * e))
    a3 = simplify((-D2 * S2 * c_0 + D2 * S2 * c_L) / (D1 * L * S1 + 2 * D2 * S2 * e))
    b1 = c_0
    b2 = simplify(
        (
            D1 * L * S1 * S2 * c_0
            + D1 * S1 * S2 * c_0 * e
            - D1 * S1 * S2 * c_L * e
            + D2 * S2**2 * c_0 * e
            + D2 * S2**2 * c_L * e
        )
        / (D1 * L * S1**2 + 2 * D2 * S1 * S2 * e)
    )
    b3 = simplify(
        (
            D1 * L * S1 * c_L
            + D2 * L * S2 * c_0
            - D2 * L * S2 * c_L
            + 2 * D2 * S2 * c_0 * e
        )
        / (D1 * L * S1 + 2 * D2 * S2 * e)
    )

    # print(latex(a1))
    # print(latex(a2))
    # print(latex(a3))
    # print(latex(b1))
    # print(latex(b2))
    # print(latex(b3))

    print("a1 = ", a1)
    print("a2 = ", a2)
    print("a3 = ", a3)
    print("b1 = ", b1)
    print("b2 = ", b2)
    print("b3 = ", b3)


def print_cylindrical_latex():
    a1_standard = simplify(
        -D2
        * S2
        * c_0
        / (
            -D1 * S1 * log(e + r_0)
            + D1 * S1 * log(L + e + r_0)
            - D2 * S2 * log(r_0)
            + D2 * S2 * log(e + r_0)
            - D2 * S2 * log(L + e + r_0)
            + D2 * S2 * log(L + 2 * e + r_0)
        )
        + D2
        * S2
        * c_L
        / (
            -D1 * S1 * log(e + r_0)
            + D1 * S1 * log(L + e + r_0)
            - D2 * S2 * log(r_0)
            + D2 * S2 * log(e + r_0)
            - D2 * S2 * log(L + e + r_0)
            + D2 * S2 * log(L + 2 * e + r_0)
        )
    )
    a1_simplified = (
        alpha
        * beta
        * (c_0 - c_L)
        / (
            alpha * beta * log(L * gamma_2)
            - alpha * beta * log(L * (gamma_1 + gamma_2))
            + alpha * beta * log(L * (gamma_1 + gamma_2 + 1))
            - alpha * beta * log(L * (2 * gamma_1 + gamma_2 + 1))
            + log(L * (gamma_1 + gamma_2))
            - log(L * (gamma_1 + gamma_2 + 1))
        )
    )
    a1_1 = logcombine(
        log(L * gamma_2)
        - log(L * (gamma_1 + gamma_2))
        + log(L * (gamma_1 + gamma_2 + 1))
        - log(L * (2 * gamma_1 + gamma_2 + 1)),
        force=True,
    )
    a1_2 = logcombine(
        log(L * (gamma_1 + gamma_2)) - log(L * (gamma_1 + gamma_2 + 1)), force=True
    )
    a1 = (
        alpha
        * beta
        * (c_0 - c_L)
        / (
            alpha
            * beta
            * (
                log(
                    gamma_2
                    * (gamma_1 + gamma_2 + 1)
                    / ((gamma_1 + gamma_2) * (2 * gamma_1 + gamma_2 + 1))
                )
            )
            + log((gamma_1 + gamma_2) / (gamma_1 + gamma_2 + 1))
        )
    )
    a2_standard = simplify(
        -D1
        * S2
        * c_0
        / (
            -D1 * S1 * log(e + r_0)
            + D1 * S1 * log(L + e + r_0)
            - D2 * S2 * log(r_0)
            + D2 * S2 * log(e + r_0)
            - D2 * S2 * log(L + e + r_0)
            + D2 * S2 * log(L + 2 * e + r_0)
        )
        + D1
        * S2
        * c_L
        / (
            -D1 * S1 * log(e + r_0)
            + D1 * S1 * log(L + e + r_0)
            - D2 * S2 * log(r_0)
            + D2 * S2 * log(e + r_0)
            - D2 * S2 * log(L + e + r_0)
            + D2 * S2 * log(L + 2 * e + r_0)
        )
    )
    a2_simplified = (
        beta
        * (c_0 - c_L)
        / (
            alpha * beta * log(L * gamma_2)
            - alpha * beta * log(L * (gamma_1 + gamma_2))
            + alpha * beta * log(L * (gamma_1 + gamma_2 + 1))
            - alpha * beta * log(L * (2 * gamma_1 + gamma_2 + 1))
            + log(L * (gamma_1 + gamma_2))
            - log(L * (gamma_1 + gamma_2 + 1))
        )
    )
    a2_1 = logcombine(
        log(L * gamma_2)
        - log(L * (gamma_1 + gamma_2))
        + log(L * (gamma_1 + gamma_2 + 1))
        - log(L * (2 * gamma_1 + gamma_2 + 1)),
        force=True,
    )
    a2_2 = logcombine(
        +log(L * (gamma_1 + gamma_2)) - log(L * (gamma_1 + gamma_2 + 1)), force=True
    )
    a2 = (
        beta
        * (c_0 - c_L)
        / (
            alpha
            * beta
            * log(
                gamma_2
                * (gamma_1 + gamma_2 + 1)
                / ((gamma_1 + gamma_2) * (2 * gamma_1 + gamma_2 + 1))
            )
            + log((gamma_1 + gamma_2) / (gamma_1 + gamma_2 + 1))
        )
    )

    a3_standard = simplify(
        -D2
        * S2
        * c_0
        / (
            -D1 * S1 * log(e + r_0)
            + D1 * S1 * log(L + e + r_0)
            - D2 * S2 * log(r_0)
            + D2 * S2 * log(e + r_0)
            - D2 * S2 * log(L + e + r_0)
            + D2 * S2 * log(L + 2 * e + r_0)
        )
        + D2
        * S2
        * c_L
        / (
            -D1 * S1 * log(e + r_0)
            + D1 * S1 * log(L + e + r_0)
            - D2 * S2 * log(r_0)
            + D2 * S2 * log(e + r_0)
            - D2 * S2 * log(L + e + r_0)
            + D2 * S2 * log(L + 2 * e + r_0)
        )
    )
    a3_simplified = (
        alpha
        * beta
        * (c_0 - c_L)
        / (
            alpha * beta * log(L * gamma_2)
            - alpha * beta * log(L * (gamma_1 + gamma_2))
            + alpha * beta * log(L * (gamma_1 + gamma_2 + 1))
            - alpha * beta * log(L * (2 * gamma_1 + gamma_2 + 1))
            + log(L * (gamma_1 + gamma_2))
            - log(L * (gamma_1 + gamma_2 + 1))
        )
    )
    a3_1 = logcombine(
        log(L * gamma_2)
        - log(L * (gamma_1 + gamma_2))
        + log(L * (gamma_1 + gamma_2 + 1))
        - log(L * (2 * gamma_1 + gamma_2 + 1)),
        force=True,
    )
    a3_2 = logcombine(
        +log(L * (gamma_1 + gamma_2)) - log(L * (gamma_1 + gamma_2 + 1)), force=True
    )
    a3 = (
        alpha
        * beta
        * (c_0 - c_L)
        / (
            alpha
            * beta
            * log(
                gamma_2
                * (gamma_1 + gamma_2 + 1)
                / ((gamma_1 + gamma_2) * (2 * gamma_1 + gamma_2 + 1))
            )
            + log((gamma_1 + gamma_2) / (gamma_1 + gamma_2 + 1))
        )
    )

    b1_standard = simplify(
        -D1
        * S1
        * c_0
        * log(e + r_0)
        / (
            -D1 * S1 * log(e + r_0)
            + D1 * S1 * log(L + e + r_0)
            - D2 * S2 * log(r_0)
            + D2 * S2 * log(e + r_0)
            - D2 * S2 * log(L + e + r_0)
            + D2 * S2 * log(L + 2 * e + r_0)
        )
        + D1
        * S1
        * c_0
        * log(L + e + r_0)
        / (
            -D1 * S1 * log(e + r_0)
            + D1 * S1 * log(L + e + r_0)
            - D2 * S2 * log(r_0)
            + D2 * S2 * log(e + r_0)
            - D2 * S2 * log(L + e + r_0)
            + D2 * S2 * log(L + 2 * e + r_0)
        )
        + D2
        * S2
        * c_0
        * log(e + r_0)
        / (
            -D1 * S1 * log(e + r_0)
            + D1 * S1 * log(L + e + r_0)
            - D2 * S2 * log(r_0)
            + D2 * S2 * log(e + r_0)
            - D2 * S2 * log(L + e + r_0)
            + D2 * S2 * log(L + 2 * e + r_0)
        )
        - D2
        * S2
        * c_0
        * log(L + e + r_0)
        / (
            -D1 * S1 * log(e + r_0)
            + D1 * S1 * log(L + e + r_0)
            - D2 * S2 * log(r_0)
            + D2 * S2 * log(e + r_0)
            - D2 * S2 * log(L + e + r_0)
            + D2 * S2 * log(L + 2 * e + r_0)
        )
        + D2
        * S2
        * c_0
        * log(L + 2 * e + r_0)
        / (
            -D1 * S1 * log(e + r_0)
            + D1 * S1 * log(L + e + r_0)
            - D2 * S2 * log(r_0)
            + D2 * S2 * log(e + r_0)
            - D2 * S2 * log(L + e + r_0)
            + D2 * S2 * log(L + 2 * e + r_0)
        )
        - D2
        * S2
        * c_L
        * log(r_0)
        / (
            -D1 * S1 * log(e + r_0)
            + D1 * S1 * log(L + e + r_0)
            - D2 * S2 * log(r_0)
            + D2 * S2 * log(e + r_0)
            - D2 * S2 * log(L + e + r_0)
            + D2 * S2 * log(L + 2 * e + r_0)
        )
    )
    b1_simplified = (
        +alpha * beta * c_0 * log(L * (gamma_1 + gamma_2 + 1))
        - alpha * beta * c_0 * log(L * (gamma_1 + gamma_2))
        - alpha * beta * c_0 * log(L * (2 * gamma_1 + gamma_2 + 1))
        + c_0 * log(L * (gamma_1 + gamma_2))
        - c_0 * log(L * (gamma_1 + gamma_2 + 1))
        + alpha * beta * c_L * log(L * gamma_2)
    ) / (
        alpha * beta * log(L * gamma_2)
        - alpha * beta * log(L * (gamma_1 + gamma_2))
        + alpha * beta * log(L * (gamma_1 + gamma_2 + 1))
        - alpha * beta * log(L * (2 * gamma_1 + gamma_2 + 1))
        + log(L * (gamma_1 + gamma_2))
        - log(L * (gamma_1 + gamma_2 + 1))
    )

    b1_t_1 = logcombine(
        log(L * (gamma_1 + gamma_2 + 1))
        - log(L * (gamma_1 + gamma_2))
        - log(L * (2 * gamma_1 + gamma_2 + 1)),
        force=True,
    )
    b1_t_2 = logcombine(
        +log(L * (gamma_1 + gamma_2)) - log(L * (gamma_1 + gamma_2 + 1)), force=True
    )
    b1_b_1 = logcombine(
        log(L * gamma_2)
        - log(L * (gamma_1 + gamma_2))
        + log(L * (gamma_1 + gamma_2 + 1))
        - log(L * (2 * gamma_1 + gamma_2 + 1)),
        force=True,
    )
    b1_b_2 = logcombine(
        log(L * (gamma_1 + gamma_2)) - log(L * (gamma_1 + gamma_2 + 1)), force=True
    )
    b1 = (
        c_0
        * (
            alpha
            * beta
            * log(
                (gamma_1 + gamma_2 + 1)
                / (L * (gamma_1 + gamma_2) * (2 * gamma_1 + gamma_2 + 1))
            )
            + log((gamma_1 + gamma_2) / (gamma_1 + gamma_2 + 1))
        )
        + alpha * beta * c_L * log(L * gamma_2)
    ) / (
        alpha
        * beta
        * log(
            gamma_2
            * (gamma_1 + gamma_2 + 1)
            / ((gamma_1 + gamma_2) * (2 * gamma_1 + gamma_2 + 1))
        )
        + log((gamma_1 + gamma_2) / (gamma_1 + gamma_2 + 1))
    )

    b2_standard = simplify(
        D1
        * S1
        * S2
        * c_0
        * log(L + e + r_0)
        / (
            -D1 * S1**2 * log(e + r_0)
            + D1 * S1**2 * log(L + e + r_0)
            - D2 * S1 * S2 * log(r_0)
            + D2 * S1 * S2 * log(e + r_0)
            - D2 * S1 * S2 * log(L + e + r_0)
            + D2 * S1 * S2 * log(L + 2 * e + r_0)
        )
        - D1
        * S1
        * S2
        * c_L
        * log(e + r_0)
        / (
            -D1 * S1**2 * log(e + r_0)
            + D1 * S1**2 * log(L + e + r_0)
            - D2 * S1 * S2 * log(r_0)
            + D2 * S1 * S2 * log(e + r_0)
            - D2 * S1 * S2 * log(L + e + r_0)
            + D2 * S1 * S2 * log(L + 2 * e + r_0)
        )
        - D2
        * S2**2
        * c_0
        * log(L + e + r_0)
        / (
            -D1 * S1**2 * log(e + r_0)
            + D1 * S1**2 * log(L + e + r_0)
            - D2 * S1 * S2 * log(r_0)
            + D2 * S1 * S2 * log(e + r_0)
            - D2 * S1 * S2 * log(L + e + r_0)
            + D2 * S1 * S2 * log(L + 2 * e + r_0)
        )
        + D2
        * S2**2
        * c_0
        * log(L + 2 * e + r_0)
        / (
            -D1 * S1**2 * log(e + r_0)
            + D1 * S1**2 * log(L + e + r_0)
            - D2 * S1 * S2 * log(r_0)
            + D2 * S1 * S2 * log(e + r_0)
            - D2 * S1 * S2 * log(L + e + r_0)
            + D2 * S1 * S2 * log(L + 2 * e + r_0)
        )
        - D2
        * S2**2
        * c_L
        * log(r_0)
        / (
            -D1 * S1**2 * log(e + r_0)
            + D1 * S1**2 * log(L + e + r_0)
            - D2 * S1 * S2 * log(r_0)
            + D2 * S1 * S2 * log(e + r_0)
            - D2 * S1 * S2 * log(L + e + r_0)
            + D2 * S1 * S2 * log(L + 2 * e + r_0)
        )
        + D2
        * S2**2
        * c_L
        * log(e + r_0)
        / (
            -D1 * S1**2 * log(e + r_0)
            + D1 * S1**2 * log(L + e + r_0)
            - D2 * S1 * S2 * log(r_0)
            + D2 * S1 * S2 * log(e + r_0)
            - D2 * S1 * S2 * log(L + e + r_0)
            + D2 * S1 * S2 * log(L + 2 * e + r_0)
        )
    )
    b2_simplified = (
        beta
        * (
            alpha * beta * c_0 * log(L * (gamma_1 + gamma_2 + 1))
            - alpha * beta * c_0 * log(L * (2 * gamma_1 + gamma_2 + 1))
            + alpha * beta * c_L * log(L * gamma_2)
            - alpha * beta * c_L * log(L * (gamma_1 + gamma_2))
            - c_0 * log(L * (gamma_1 + gamma_2 + 1))
            + c_L * log(L * (gamma_1 + gamma_2))
        )
        / (
            alpha * beta * log(L * gamma_2)
            - alpha * beta * log(L * (gamma_1 + gamma_2))
            + alpha * beta * log(L * (gamma_1 + gamma_2 + 1))
            - alpha * beta * log(L * (2 * gamma_1 + gamma_2 + 1))
            + log(L * (gamma_1 + gamma_2))
            - log(L * (gamma_1 + gamma_2 + 1))
        )
    )
    b2_simplified_factored = (
        beta
        * (
            c_0
            * (
                alpha * beta * log(L * (gamma_1 + gamma_2 + 1))
                - alpha * beta * log(L * (2 * gamma_1 + gamma_2 + 1))
                - log(L * (gamma_1 + gamma_2 + 1))
            )
            + c_L
            * (
                +alpha * beta * log(L * gamma_2)
                - alpha * beta * log(L * (gamma_1 + gamma_2))
                + log(L * (gamma_1 + gamma_2))
            )
        )
        / (
            alpha * beta * log(L * gamma_2)
            - alpha * beta * log(L * (gamma_1 + gamma_2))
            + alpha * beta * log(L * (gamma_1 + gamma_2 + 1))
            - alpha * beta * log(L * (2 * gamma_1 + gamma_2 + 1))
            + log(L * (gamma_1 + gamma_2))
            - log(L * (gamma_1 + gamma_2 + 1))
        )
    )
    b2_t_1 = logcombine(
        log(L * (gamma_1 + gamma_2 + 1)) - log(L * (2 * gamma_1 + gamma_2 + 1)),
        force=True,
    )
    b2_t_2 = logcombine(log(L * gamma_2) - log(L * (gamma_1 + gamma_2)), force=True)
    b2_b_1 = logcombine(
        log(L * gamma_2)
        - log(L * (gamma_1 + gamma_2))
        + log(L * (gamma_1 + gamma_2 + 1))
        - log(L * (2 * gamma_1 + gamma_2 + 1)),
        force=True,
    )
    b2_b_2 = logcombine(
        +log(L * (gamma_1 + gamma_2)) - log(L * (gamma_1 + gamma_2 + 1)), force=True
    )
    b2 = (
        beta
        * (
            c_0
            * (
                alpha
                * beta
                * log((gamma_1 + gamma_2 + 1) / (2 * gamma_1 + gamma_2 + 1))
                - log(L * (gamma_1 + gamma_2 + 1))
            )
            + c_L
            * (
                +alpha * beta * log(gamma_2 / (gamma_1 + gamma_2))
                + log(L * (gamma_1 + gamma_2))
            )
        )
        / (
            alpha
            * beta
            * log(
                gamma_2
                * (gamma_1 + gamma_2 + 1)
                / ((gamma_1 + gamma_2) * (2 * gamma_1 + gamma_2 + 1))
            )
            + log((gamma_1 + gamma_2) / (gamma_1 + gamma_2 + 1))
        )
    )

    b3_standard = simplify(
        -D1
        * S1
        * c_L
        * log(e + r_0)
        / (
            -D1 * S1 * log(e + r_0)
            + D1 * S1 * log(L + e + r_0)
            - D2 * S2 * log(r_0)
            + D2 * S2 * log(e + r_0)
            - D2 * S2 * log(L + e + r_0)
            + D2 * S2 * log(L + 2 * e + r_0)
        )
        + D1
        * S1
        * c_L
        * log(L + e + r_0)
        / (
            -D1 * S1 * log(e + r_0)
            + D1 * S1 * log(L + e + r_0)
            - D2 * S2 * log(r_0)
            + D2 * S2 * log(e + r_0)
            - D2 * S2 * log(L + e + r_0)
            + D2 * S2 * log(L + 2 * e + r_0)
        )
        + D2
        * S2
        * c_0
        * log(L + 2 * e + r_0)
        / (
            -D1 * S1 * log(e + r_0)
            + D1 * S1 * log(L + e + r_0)
            - D2 * S2 * log(r_0)
            + D2 * S2 * log(e + r_0)
            - D2 * S2 * log(L + e + r_0)
            + D2 * S2 * log(L + 2 * e + r_0)
        )
        - D2
        * S2
        * c_L
        * log(r_0)
        / (
            -D1 * S1 * log(e + r_0)
            + D1 * S1 * log(L + e + r_0)
            - D2 * S2 * log(r_0)
            + D2 * S2 * log(e + r_0)
            - D2 * S2 * log(L + e + r_0)
            + D2 * S2 * log(L + 2 * e + r_0)
        )
        + D2
        * S2
        * c_L
        * log(e + r_0)
        / (
            -D1 * S1 * log(e + r_0)
            + D1 * S1 * log(L + e + r_0)
            - D2 * S2 * log(r_0)
            + D2 * S2 * log(e + r_0)
            - D2 * S2 * log(L + e + r_0)
            + D2 * S2 * log(L + 2 * e + r_0)
        )
        - D2
        * S2
        * c_L
        * log(L + e + r_0)
        / (
            -D1 * S1 * log(e + r_0)
            + D1 * S1 * log(L + e + r_0)
            - D2 * S2 * log(r_0)
            + D2 * S2 * log(e + r_0)
            - D2 * S2 * log(L + e + r_0)
            + D2 * S2 * log(L + 2 * e + r_0)
        )
    )
    b3_simplified = (
        -alpha * beta * c_0 * log(L * (2 * gamma_1 + gamma_2 + 1))
        + alpha * beta * c_L * log(L * gamma_2)
        - alpha * beta * c_L * log(L * (gamma_1 + gamma_2))
        + alpha * beta * c_L * log(L * (gamma_1 + gamma_2 + 1))
        + c_L * log(L * (gamma_1 + gamma_2))
        - c_L * log(L * (gamma_1 + gamma_2 + 1))
    ) / (
        alpha * beta * log(L * gamma_2)
        - alpha * beta * log(L * (gamma_1 + gamma_2))
        + alpha * beta * log(L * (gamma_1 + gamma_2 + 1))
        - alpha * beta * log(L * (2 * gamma_1 + gamma_2 + 1))
        + log(L * (gamma_1 + gamma_2))
        - log(L * (gamma_1 + gamma_2 + 1))
    )
    b3_simplified_factored = (
        -alpha * beta * c_0 * log(L * (2 * gamma_1 + gamma_2 + 1))
        + c_L
        * (
            alpha * beta * log(L * gamma_2)
            - alpha * beta * log(L * (gamma_1 + gamma_2))
            + alpha * beta * log(L * (gamma_1 + gamma_2 + 1))
            + log(L * (gamma_1 + gamma_2))
            - log(L * (gamma_1 + gamma_2 + 1))
        )
    ) / (
        alpha * beta * log(L * gamma_2)
        - alpha * beta * log(L * (gamma_1 + gamma_2))
        + alpha * beta * log(L * (gamma_1 + gamma_2 + 1))
        - alpha * beta * log(L * (2 * gamma_1 + gamma_2 + 1))
        + log(L * (gamma_1 + gamma_2))
        - log(L * (gamma_1 + gamma_2 + 1))
    )
    b3_t_1 = logcombine(
        log(L * gamma_2)
        - log(L * (gamma_1 + gamma_2))
        + log(L * (gamma_1 + gamma_2 + 1)),
        force=True,
    )
    b3_t_2 = logcombine(
        log(L * (gamma_1 + gamma_2)) - log(L * (gamma_1 + gamma_2 + 1)), force=True
    )

    b3_b_1 = logcombine(
        log(L * gamma_2)
        - log(L * (gamma_1 + gamma_2))
        + log(L * (gamma_1 + gamma_2 + 1))
        - log(L * (2 * gamma_1 + gamma_2 + 1)),
        force=True,
    )
    b3_b_2 = logcombine(
        log(L * (gamma_1 + gamma_2)) - log(L * (gamma_1 + gamma_2 + 1)), force=True
    )
    b3 = (
        -alpha * beta * c_0 * log(L * (2 * gamma_1 + gamma_2 + 1))
        + c_L
        * (
            alpha
            * beta
            * log(L * gamma_2 * (gamma_1 + gamma_2 + 1) / (gamma_1 + gamma_2))
            + log((gamma_1 + gamma_2) / (gamma_1 + gamma_2 + 1))
        )
    ) / (
        alpha
        * beta
        * log(
            gamma_2
            * (gamma_1 + gamma_2 + 1)
            / ((gamma_1 + gamma_2) * (2 * gamma_1 + gamma_2 + 1))
        )
        + log((gamma_1 + gamma_2) / (gamma_1 + gamma_2 + 1))
    )

    print("a_{1} = ", latex(a1))
    print("a_{2} = ", latex(a2))
    print("a_{3} = ", latex(a3))
    print("b_{1} = ", latex(b1))
    print("b_{2} = ", latex(b2))
    print("b_{3} = ", latex(b3))


def print_fluxes_cylindirical_latex():
    P = Symbol("P")
    coated = simplify(
        D1
        * D2
        * P**0.5
        * S1
        * S2
        / (
            -D1 * S1 * log(r_0)
            + D1 * S1 * log(L + r_0)
            + D2 * S2 * log(r_0)
            - D2 * S2 * log(L + r_0)
            - D2 * S2 * log(-e + r_0)
            + D2 * S2 * log(L + e + r_0)
        )
    )
    coated_simplified = (
        D1
        * P**0.5
        * S1
        * alpha
        * beta
        / (
            alpha * beta * log(L * gamma_2)
            - alpha * beta * log(L * (-gamma_1 + gamma_2))
            - alpha * beta * log(L * (gamma_2 + 1))
            + alpha * beta * log(L * (gamma_1 + gamma_2 + 1))
            - log(L * gamma_2)
            + log(L * (gamma_2 + 1))
        )
    )
    coated_simplified_combined = (
        D1
        * P**0.5
        * S1
        * alpha
        * beta
        / (
            alpha
            * beta
            * log(
                gamma_2
                * (gamma_1 + gamma_2 + 1)
                / ((-gamma_1 + gamma_2) * (gamma_2 + 1))
            )
            + log((gamma_2 + 1) / gamma_2)
        )
    )
    c1 = logcombine(
        log(L * gamma_2)
        - log(L * (-gamma_1 + gamma_2))
        - log(L * (gamma_2 + 1))
        + log(L * (gamma_1 + gamma_2 + 1)),
        force=True,
    )
    c2 = logcombine(-log(L * gamma_2) + log(L * (gamma_2 + 1)), force=True)

    uncoated = simplify(
        D2**2 * P**0.5 * S2**2 / (-D2 * S2 * log(r_0) + D2 * S2 * log(L + r_0))
    )
    uncoated_simplified = (
        D1 * P**0.5 * S1 * alpha * beta / (-log(L * gamma_2) + log(L * (gamma_2 + 1)))
    )
    uc1 = logcombine(-log(L * gamma_2) + log(L * (gamma_2 + 1)), force=True)
    uncoated_simplified_combined = (
        D1 * P**0.5 * S1 * alpha * beta / log((gamma_2 + 1) / gamma_2)
    )

    print(latex(coated_simplified_combined))
    print(latex(uncoated_simplified_combined))


def print_PRF_cylindrical_latex():
    PRF = simplify(
        (
            D1 * S1 * log(r_0)
            - D1 * S1 * log(L + r_0)
            - D2 * S2 * log(r_0)
            + D2 * S2 * log(L + r_0)
            + D2 * S2 * log(-e + r_0)
            - D2 * S2 * log(L + e + r_0)
        )
        / (D1 * S1 * (log(r_0) - log(L + r_0)))
    )

    PRF_simplified = (
        -alpha * beta * log(L * gamma_2)
        + alpha * beta * log(L * (-gamma_1 + gamma_2))
        + alpha * beta * log(L * (gamma_2 + 1))
        - alpha * beta * log(L * (gamma_1 + gamma_2 + 1))
        + log(L * gamma_2)
        - log(L * (gamma_2 + 1))
    ) / (log(L * gamma_2) - log(L * (gamma_2 + 1)))

    prf_t_1 = logcombine(
        log(L * (-gamma_1 + gamma_2))
        - log(L * gamma_2)
        + log(L * (gamma_2 + 1))
        - log(L * (gamma_1 + gamma_2 + 1)),
        force=True,
    )
    print(PRF)


print_cylindrical_latex()
