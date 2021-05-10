import esl

from esl.economics.markets.walras import excess_demand_model, differentiable_order_message


class Fund(esl.economics.company):
    def __init__(self, identifier, jurisdiction = esl.law.jurisdictions.US):
        super().__init__(identifier, jurisdiction)
        pass


class NoiseTrader(Fund):

    def __init__(self, identifier):
        super().__init__(identifier)

    def act(self, si: esl.simulation.time_interval, s: esl.seed):

        pass

    class NoiseTraderOrder(differentiable_order_message):

        def __init__(self, sender, recipient, sent, received):
            super().__init__(sender, recipient, sent, received)
            self.sender = sender

        def excess_demand(self, quotes):
            """

            :param quotes: A dict with property_identifier keys and pairs (quote, variable)
            :return:
            """
            print(f"The Walrasian price setter suggests the following prices: {quotes}")
            ed = {k: ((i+3.) - (float(v[0]) * v[1])) for i,  (k, v) in enumerate(quotes.items())}
            print(f"Agent {self.sender}'s excess demand at these prices is: {ed}")
            return ed




class SingleExperiment(esl.simulation.model):
    def __init__(self, environment, parameters):
        super().__init__(environment, parameters)
        #self.economy = esl.simulation.world()

    def clear_market(initial_prices, excess_demand_functions):
        model = esl.economics.markets.walras.excess_demand_model(initial_prices)
        model.excess_demand_functions = excess_demand_functions
        return model.compute_clearing_quotes()

    def step(self, time_interval):
        """
            Here we do model-specific logic, such as deciding when to stop the simulation early
        :param time_interval:
        :return:
        """
        # Here we do model-specific logic

        print(f"step {time_interval}")
        return time_interval.upper



if __name__ == "__main__":


    environment = esl.computation.environment()
    parameters = esl.simulation.parameter.parametrization()

    model = SingleExperiment(environment, parameters)

    print(model.world)
    print(model.world.create())

    nt = NoiseTrader(esl.simulation.identity([1,2]))





    se = esl.simulation.time_interval(1,10)

    print(  environment.run  )

    a = model.step(se)
    print(model.start)


