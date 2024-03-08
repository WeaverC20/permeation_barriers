import numpy as np

c_0 = 4
c_L = 4.5
D1 = 2
D2 = 2.5
alpha = D2 / D1
S1 = 3
S2 = 3.5
beta = S2 / S1
e = 5
L = 5.5
gamma = e / L
gamma_1 = gamma
r_0 = 6
gamma_2 = r_0 / L


def cartesian():
    a1_standard = (-D2 * S2 * c_0 + D2 * S2 * c_L) / (D1 * L * S1 + 2 * D2 * S2 * e)
    a2_standard = (-D1 * S2 * c_0 + D1 * S2 * c_L) / (D1 * L * S1 + 2 * D2 * S2 * e)
    a3_standard = (-D2 * S2 * c_0 + D2 * S2 * c_L) / (D1 * L * S1 + 2 * D2 * S2 * e)
    b1_standard = c_0
    b2_standard = (
        D1 * L * S1 * S2 * c_0
        + D1 * S1 * S2 * c_0 * e
        - D1 * S1 * S2 * c_L * e
        + D2 * S2**2 * c_0 * e
        + D2 * S2**2 * c_L * e
    ) / (D1 * L * S1**2 + 2 * D2 * S1 * S2 * e)
    b3_standard = (
        D1 * L * S1 * c_L
        + D2 * L * S2 * c_0
        - D2 * L * S2 * c_L
        + 2 * D2 * S2 * c_0 * e
    ) / (D1 * L * S1 + 2 * D2 * S2 * e)

    a1 = alpha * beta * (-c_0 + c_L) / (L * (2 * alpha * beta * gamma + 1))
    a2 = beta * (-c_0 + c_L) / (L * (2 * alpha * beta * gamma + 1))
    a3 = alpha * beta * (-c_0 + c_L) / (L * (2 * alpha * beta * gamma + 1))
    b1 = c_0
    b2 = (
        beta
        * (
            alpha * beta * c_0 * gamma
            + alpha * beta * c_L * gamma
            + c_0 * gamma
            + c_0
            - c_L * gamma
        )
        / (2 * alpha * beta * gamma + 1)
    )
    b3 = (
        2 * alpha * beta * c_0 * gamma + alpha * beta * c_0 - alpha * beta * c_L + c_L
    ) / (2 * alpha * beta * gamma + 1)


def cylindrical():
    a1 = (
        alpha
        * beta
        * (c_0 - c_L)
        / (
            alpha
            * beta
            * (
                np.log(
                    gamma_2
                    * (gamma_1 + gamma_2 + 1)
                    / ((gamma_1 + gamma_2) * (2 * gamma_1 + gamma_2 + 1))
                )
            )
            + np.log((gamma_1 + gamma_2) / (gamma_1 + gamma_2 + 1))
        )
    )
    a2 = (
        beta
        * (c_0 - c_L)
        / (
            alpha
            * beta
            * np.log(
                gamma_2
                * (gamma_1 + gamma_2 + 1)
                / ((gamma_1 + gamma_2) * (2 * gamma_1 + gamma_2 + 1))
            )
            + np.log((gamma_1 + gamma_2) / (gamma_1 + gamma_2 + 1))
        )
    )
    a3 = (
        alpha
        * beta
        * (c_0 - c_L)
        / (
            alpha
            * beta
            * np.log(
                gamma_2
                * (gamma_1 + gamma_2 + 1)
                / ((gamma_1 + gamma_2) * (2 * gamma_1 + gamma_2 + 1))
            )
            + np.log((gamma_1 + gamma_2) / (gamma_1 + gamma_2 + 1))
        )
    )
    b1 = (
        c_0
        * (
            alpha
            * beta
            * np.log(
                (gamma_1 + gamma_2 + 1)
                / (L * (gamma_1 + gamma_2) * (2 * gamma_1 + gamma_2 + 1))
            )
            + np.log((gamma_1 + gamma_2) / (gamma_1 + gamma_2 + 1))
        )
        + alpha * beta * c_L * np.log(L * gamma_2)
    ) / (
        alpha
        * beta
        * np.log(
            gamma_2
            * (gamma_1 + gamma_2 + 1)
            / ((gamma_1 + gamma_2) * (2 * gamma_1 + gamma_2 + 1))
        )
        + np.log((gamma_1 + gamma_2) / (gamma_1 + gamma_2 + 1))
    )
    b2 = (
        beta
        * (
            c_0
            * (
                alpha
                * beta
                * np.log((gamma_1 + gamma_2 + 1) / (2 * gamma_1 + gamma_2 + 1))
                - np.log(L * (gamma_1 + gamma_2 + 1))
            )
            + c_L
            * (
                +alpha * beta * np.log(gamma_2 / (gamma_1 + gamma_2))
                + np.log(L * (gamma_1 + gamma_2))
            )
        )
        / (
            alpha
            * beta
            * np.log(
                gamma_2
                * (gamma_1 + gamma_2 + 1)
                / ((gamma_1 + gamma_2) * (2 * gamma_1 + gamma_2 + 1))
            )
            + np.log((gamma_1 + gamma_2) / (gamma_1 + gamma_2 + 1))
        )
    )
    b3 = (
        -alpha * beta * c_0 * np.log(L * (2 * gamma_1 + gamma_2 + 1))
        + c_L
        * (
            alpha
            * beta
            * np.log(L * gamma_2 * (gamma_1 + gamma_2 + 1) / (gamma_1 + gamma_2))
            + np.log((gamma_1 + gamma_2) / (gamma_1 + gamma_2 + 1))
        )
    ) / (
        alpha
        * beta
        * np.log(
            gamma_2
            * (gamma_1 + gamma_2 + 1)
            / ((gamma_1 + gamma_2) * (2 * gamma_1 + gamma_2 + 1))
        )
        + np.log((gamma_1 + gamma_2) / (gamma_1 + gamma_2 + 1))
    )
    a1_standard = -D2 * S2 * c_0 / (
        -D1 * S1 * np.log(e + r_0)
        + D1 * S1 * np.log(L + e + r_0)
        - D2 * S2 * np.log(r_0)
        + D2 * S2 * np.log(e + r_0)
        - D2 * S2 * np.log(L + e + r_0)
        + D2 * S2 * np.log(L + 2 * e + r_0)
    ) + D2 * S2 * c_L / (
        -D1 * S1 * np.log(e + r_0)
        + D1 * S1 * np.log(L + e + r_0)
        - D2 * S2 * np.log(r_0)
        + D2 * S2 * np.log(e + r_0)
        - D2 * S2 * np.log(L + e + r_0)
        + D2 * S2 * np.log(L + 2 * e + r_0)
    )
    a2_standard = -D1 * S2 * c_0 / (
        -D1 * S1 * np.log(e + r_0)
        + D1 * S1 * np.log(L + e + r_0)
        - D2 * S2 * np.log(r_0)
        + D2 * S2 * np.log(e + r_0)
        - D2 * S2 * np.log(L + e + r_0)
        + D2 * S2 * np.log(L + 2 * e + r_0)
    ) + D1 * S2 * c_L / (
        -D1 * S1 * np.log(e + r_0)
        + D1 * S1 * np.log(L + e + r_0)
        - D2 * S2 * np.log(r_0)
        + D2 * S2 * np.log(e + r_0)
        - D2 * S2 * np.log(L + e + r_0)
        + D2 * S2 * np.log(L + 2 * e + r_0)
    )
    a3_standard = -D2 * S2 * c_0 / (
        -D1 * S1 * np.log(e + r_0)
        + D1 * S1 * np.log(L + e + r_0)
        - D2 * S2 * np.log(r_0)
        + D2 * S2 * np.log(e + r_0)
        - D2 * S2 * np.log(L + e + r_0)
        + D2 * S2 * np.log(L + 2 * e + r_0)
    ) + D2 * S2 * c_L / (
        -D1 * S1 * np.log(e + r_0)
        + D1 * S1 * np.log(L + e + r_0)
        - D2 * S2 * np.log(r_0)
        + D2 * S2 * np.log(e + r_0)
        - D2 * S2 * np.log(L + e + r_0)
        + D2 * S2 * np.log(L + 2 * e + r_0)
    )
    b1_standard = (
        -D1
        * S1
        * c_0
        * np.log(e + r_0)
        / (
            -D1 * S1 * np.log(e + r_0)
            + D1 * S1 * np.log(L + e + r_0)
            - D2 * S2 * np.log(r_0)
            + D2 * S2 * np.log(e + r_0)
            - D2 * S2 * np.log(L + e + r_0)
            + D2 * S2 * np.log(L + 2 * e + r_0)
        )
        + D1
        * S1
        * c_0
        * np.log(L + e + r_0)
        / (
            -D1 * S1 * np.log(e + r_0)
            + D1 * S1 * np.log(L + e + r_0)
            - D2 * S2 * np.log(r_0)
            + D2 * S2 * np.log(e + r_0)
            - D2 * S2 * np.log(L + e + r_0)
            + D2 * S2 * np.log(L + 2 * e + r_0)
        )
        + D2
        * S2
        * c_0
        * np.log(e + r_0)
        / (
            -D1 * S1 * np.log(e + r_0)
            + D1 * S1 * np.log(L + e + r_0)
            - D2 * S2 * np.log(r_0)
            + D2 * S2 * np.log(e + r_0)
            - D2 * S2 * np.log(L + e + r_0)
            + D2 * S2 * np.log(L + 2 * e + r_0)
        )
        - D2
        * S2
        * c_0
        * np.log(L + e + r_0)
        / (
            -D1 * S1 * np.log(e + r_0)
            + D1 * S1 * np.log(L + e + r_0)
            - D2 * S2 * np.log(r_0)
            + D2 * S2 * np.log(e + r_0)
            - D2 * S2 * np.log(L + e + r_0)
            + D2 * S2 * np.log(L + 2 * e + r_0)
        )
        + D2
        * S2
        * c_0
        * np.log(L + 2 * e + r_0)
        / (
            -D1 * S1 * np.log(e + r_0)
            + D1 * S1 * np.log(L + e + r_0)
            - D2 * S2 * np.log(r_0)
            + D2 * S2 * np.log(e + r_0)
            - D2 * S2 * np.log(L + e + r_0)
            + D2 * S2 * np.log(L + 2 * e + r_0)
        )
        - D2
        * S2
        * c_L
        * np.log(r_0)
        / (
            -D1 * S1 * np.log(e + r_0)
            + D1 * S1 * np.log(L + e + r_0)
            - D2 * S2 * np.log(r_0)
            + D2 * S2 * np.log(e + r_0)
            - D2 * S2 * np.log(L + e + r_0)
            + D2 * S2 * np.log(L + 2 * e + r_0)
        )
    )
    b2_standard = (
        D1
        * S1
        * S2
        * c_0
        * np.log(L + e + r_0)
        / (
            -D1 * S1**2 * np.log(e + r_0)
            + D1 * S1**2 * np.log(L + e + r_0)
            - D2 * S1 * S2 * np.log(r_0)
            + D2 * S1 * S2 * np.log(e + r_0)
            - D2 * S1 * S2 * np.log(L + e + r_0)
            + D2 * S1 * S2 * np.log(L + 2 * e + r_0)
        )
        - D1
        * S1
        * S2
        * c_L
        * np.log(e + r_0)
        / (
            -D1 * S1**2 * np.log(e + r_0)
            + D1 * S1**2 * np.log(L + e + r_0)
            - D2 * S1 * S2 * np.log(r_0)
            + D2 * S1 * S2 * np.log(e + r_0)
            - D2 * S1 * S2 * np.log(L + e + r_0)
            + D2 * S1 * S2 * np.log(L + 2 * e + r_0)
        )
        - D2
        * S2**2
        * c_0
        * np.log(L + e + r_0)
        / (
            -D1 * S1**2 * np.log(e + r_0)
            + D1 * S1**2 * np.log(L + e + r_0)
            - D2 * S1 * S2 * np.log(r_0)
            + D2 * S1 * S2 * np.log(e + r_0)
            - D2 * S1 * S2 * np.log(L + e + r_0)
            + D2 * S1 * S2 * np.log(L + 2 * e + r_0)
        )
        + D2
        * S2**2
        * c_0
        * np.log(L + 2 * e + r_0)
        / (
            -D1 * S1**2 * np.log(e + r_0)
            + D1 * S1**2 * np.log(L + e + r_0)
            - D2 * S1 * S2 * np.log(r_0)
            + D2 * S1 * S2 * np.log(e + r_0)
            - D2 * S1 * S2 * np.log(L + e + r_0)
            + D2 * S1 * S2 * np.log(L + 2 * e + r_0)
        )
        - D2
        * S2**2
        * c_L
        * np.log(r_0)
        / (
            -D1 * S1**2 * np.log(e + r_0)
            + D1 * S1**2 * np.log(L + e + r_0)
            - D2 * S1 * S2 * np.log(r_0)
            + D2 * S1 * S2 * np.log(e + r_0)
            - D2 * S1 * S2 * np.log(L + e + r_0)
            + D2 * S1 * S2 * np.log(L + 2 * e + r_0)
        )
        + D2
        * S2**2
        * c_L
        * np.log(e + r_0)
        / (
            -D1 * S1**2 * np.log(e + r_0)
            + D1 * S1**2 * np.log(L + e + r_0)
            - D2 * S1 * S2 * np.log(r_0)
            + D2 * S1 * S2 * np.log(e + r_0)
            - D2 * S1 * S2 * np.log(L + e + r_0)
            + D2 * S1 * S2 * np.log(L + 2 * e + r_0)
        )
    )
    b3_standard = (
        -D1
        * S1
        * c_L
        * np.log(e + r_0)
        / (
            -D1 * S1 * np.log(e + r_0)
            + D1 * S1 * np.log(L + e + r_0)
            - D2 * S2 * np.log(r_0)
            + D2 * S2 * np.log(e + r_0)
            - D2 * S2 * np.log(L + e + r_0)
            + D2 * S2 * np.log(L + 2 * e + r_0)
        )
        + D1
        * S1
        * c_L
        * np.log(L + e + r_0)
        / (
            -D1 * S1 * np.log(e + r_0)
            + D1 * S1 * np.log(L + e + r_0)
            - D2 * S2 * np.log(r_0)
            + D2 * S2 * np.log(e + r_0)
            - D2 * S2 * np.log(L + e + r_0)
            + D2 * S2 * np.log(L + 2 * e + r_0)
        )
        + D2
        * S2
        * c_0
        * np.log(L + 2 * e + r_0)
        / (
            -D1 * S1 * np.log(e + r_0)
            + D1 * S1 * np.log(L + e + r_0)
            - D2 * S2 * np.log(r_0)
            + D2 * S2 * np.log(e + r_0)
            - D2 * S2 * np.log(L + e + r_0)
            + D2 * S2 * np.log(L + 2 * e + r_0)
        )
        - D2
        * S2
        * c_L
        * np.log(r_0)
        / (
            -D1 * S1 * np.log(e + r_0)
            + D1 * S1 * np.log(L + e + r_0)
            - D2 * S2 * np.log(r_0)
            + D2 * S2 * np.log(e + r_0)
            - D2 * S2 * np.log(L + e + r_0)
            + D2 * S2 * np.log(L + 2 * e + r_0)
        )
        + D2
        * S2
        * c_L
        * np.log(e + r_0)
        / (
            -D1 * S1 * np.log(e + r_0)
            + D1 * S1 * np.log(L + e + r_0)
            - D2 * S2 * np.log(r_0)
            + D2 * S2 * np.log(e + r_0)
            - D2 * S2 * np.log(L + e + r_0)
            + D2 * S2 * np.log(L + 2 * e + r_0)
        )
        - D2
        * S2
        * c_L
        * np.log(L + e + r_0)
        / (
            -D1 * S1 * np.log(e + r_0)
            + D1 * S1 * np.log(L + e + r_0)
            - D2 * S2 * np.log(r_0)
            + D2 * S2 * np.log(e + r_0)
            - D2 * S2 * np.log(L + e + r_0)
            + D2 * S2 * np.log(L + 2 * e + r_0)
        )
    )

    # if np.isclose(a1, a1_standard):
    #     print("coucou")
    # else:
    #     print("failed")
    print(a2)
    print(a2_standard)
    print(a3)
    print(a3_standard)


# cartesian()
cylindrical()
