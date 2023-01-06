from typing import Optional
import strawberry

@strawberry.type
class Country:
    name: str


counter = 0


@strawberry.type
class Query:
    @strawberry.field
    def country(self, code: str) -> Optional[Country]:
        name = {
            "GB": "United Kingdom",
            "US": "United States",
            "IT": "Italy",
            "FR": "France",
            "DE": "Germany",
            "ES": "Spain",
            "CH": "Switzerland",
            "NL": "Netherlands",
            "BE": "Belgium",
            "AT": "Austria",
            "SE": "Sweden",
            "DK": "Denmark",
            "NO": "Norway",
            "FI": "Finland",
            "IE": "Ireland",
            "PT": "Portugal",
            "GR": "Greece",
            "LU": "Luxembourg",
            "CY": "Cyprus",
            "MT": "Malta",
            "EE": "Estonia",
            "LV": "Latvia",
            "LT": "Lithuania",
            "PL": "Poland",
            "CZ": "Czech Republic",
        }.get(code.upper())


        global counter
        counter += 1

        if name:
            name = f"{name} {counter}"

            print(name)

            return Country(name=name)

        return None

schema = strawberry.Schema(
    Query
)
