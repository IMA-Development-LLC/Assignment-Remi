class methods:
    @staticmethod
    def numeric_list(fisk1: str, fisk2: str, fisk3: str, fisk4: str, fisk5: str) -> str:
        """
        Oppretter en nummerert liste av fem elementer.

        :param fisk1: Første element i listen
        :param fisk2: Andre element i listen
        :param fisk3: Tredje element i listen
        :param fisk4: Fjerde element i listen
        :param fisk5: Femte element i listen
        :return: Nummerert liste som en streng
        """
        return f'1. {fisk1}\n2. {fisk2}\n3. {fisk3}\n4. {fisk4}\n5. {fisk5}\n'

    @staticmethod
    def absence(undocumented_absence: float, documented_absence: float, total_hours: int) -> str:
        """
        Evaluere fravær og generere en passende melding basert på prosentvis fravær.

        :param undocumented_absence: Antall timer med udocumentert fravær
        :param documented_absence: Antall timer med dokumentert fravær
        :param total_hours: Totalt antall timer i perioden
        :return: Melding basert på fraværsprosenten som en streng
        """

        # Calculate percent by dividing total undocumented hours by total hours then multiplying by 100.
        undocumented_absence_percent = (undocumented_absence / total_hours) * 100

        # Calculate percent by dividing total documented hours by total hours then multiplying by 100.
        documented_absence_percent = (documented_absence / total_hours) * 100

        # debugging: print(undocumented_absence_percent)
        # debugging: print(documented_absence_percent)

        if undocumented_absence_percent >= 10 or (undocumented_absence_percent >= 5 and documented_absence_percent >= 20):
            return f'Mister karakteren i faget | {undocumented_absence_percent}%'
        elif documented_absence_percent >= 20:
            return f'Send varsel om fare for å miste karakteren grunnet manglende vurderingsgrunnlag | {undocumented_absence_percent}%'
        elif undocumented_absence_percent >= 5:
            return f'Send varsel om fare for å miste karakteren grunnet fravær | {undocumented_absence_percent}%'
        else:
            return ''

    @staticmethod
    def baufort(meters_per_second: int) -> str:
        """
        Oversetter vindhastighet fra meter per sekund til Beaufort skalaen.

        :param meters_per_second: Vindhastighet i meter per sekund
        :return: Tilsvarende Beaufort beskrivelse som en streng
        """
        baufort_limit = {
            0.3: "Stille",
            1.6: "Flau vind",
            3.4: "Svak vind",
            5.5: "Lett bris",
            8.0: "Laber bris",
            10.8: "Frisk bris",
            13.9: "Liten kuling",
            17.2: "Stiv kuling",
            20.8: "Sterk kuling",
            24.5: "Liten storm",
            28.5: "Full storm",
            32.7: "Sterk storm",
        }

        # Sjekker vindhastigheten mot baufort grensene og returnerer tilsvarende beskrivelse.
        for limit, beaufort in baufort_limit.items():
            if meters_per_second < limit:
                return beaufort
        return "Orkan"

