library(rjson)
library(plyr)
setwd("C:/Path/to/dir/")

json_file <- "R_VCG_phyl_input.txt"
json_data <- fromJSON(file= json_file)
asFrame <- do.call("rbind.fill", lapply(json_data, as.data.frame))
asFrame[is.na(asFrame)] <- 0

asFrame_rownames <- asFrame[,-1]
rownames(asFrame_rownames) <- asFrame[,1]


plot(hclust(dist(asFrame_rownames),method="average"))
