library(data.table)

# for each climate
climates <- c('arctic','subarctic','temperate','subtropical','tropical')
terrains <- c('desert','forest','plains','hills','mountains','seacoast')

for (i in climates){
  for (j in terrains){
    input_file <- paste0(i,"_",j,"_weather_5year.txt")
    data <- fread(input_file)
    
    data$wind
    data$wind_max <- data$wind
    data$wind_low <- data$wind / 2
    
    wind <- fread("wind.csv")
    
    data <- merge(data,wind,by="wind_max", all.x = T)
    data <- data[order(day)]
    
    rain <- fread("precip.csv")
    
    data <- merge(data,rain,by="precip", all.x = T)
    data <- data[order(day)]
    
    output_file <- paste0(i,"_",j,"_weather_5year.csv")
    
    fwrite(data, output_file)
    
  }
}
