mutation = """ 
query Tariffs($postcode: String!, $monthly: Boolean!, $legacyPrepay: Boolean!, $smartPayg: Boolean!, $eco7: Boolean!) {
  tariffs(postcode: $postcode) {
    residential {
      electricity {
        credit @include(if: $monthly) {
          standard @skip(if: $eco7) {
            ...StandardElectricityTariff
            __typename
          }
          economy7 @include(if: $eco7) {
            ...Eco7ElectricityTariff
            __typename
          }
          __typename
        }
        prepay @include(if: $legacyPrepay) {
          standard @skip(if: $eco7) {
            ...StandardElectricityTariff
            __typename
          }
          economy7 @include(if: $eco7) {
            ...Eco7ElectricityTariff
            __typename
          }
          __typename
        }
        smartPayg @include(if: $smartPayg) {
          standard @skip(if: $eco7) {
            ...StandardElectricityTariff
            __typename
          }
          economy7 @include(if: $eco7) {
            ...Eco7ElectricityTariff
            __typename
          }
          __typename
        }
        __typename
      }
      __typename
    }
    __typename
  }
}

fragment StandardElectricityTariff on ResidentialElectricityStandardTariff {
  fuel
  postcode
  paymentMethod
  standingCharge
  unitRates {
    standard
    __typename
  }
  __typename
}

fragment Eco7ElectricityTariff on ResidentialElectricityEconomy7Tariff {
  fuel
  postcode
  paymentMethod
  standingCharge
  unitRates {
    day
    night
    __typename
  }
  __typename
}
""".strip()
