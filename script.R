library("irace")
setwd("~/Documents/TCC/Simuladores/OpenAiEsNe/tuning")
scenario <- readScenario(filename = "scenario.txt",
scenario = defaultScenario())
irace.main(scenario = scenario)