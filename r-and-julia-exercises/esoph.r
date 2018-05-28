cat("List all columns: \n\n")

print(head(esoph, 88))

cat("\nSummary of esoph data: \n\n")

print(summary(esoph))

cat("\nAverage number of cases: \n\n")

print(mean(esoph$ncases))

cat("\nAverage number of cases between 25-34: \n\n")

print(mean(esoph$ncases[1:15]))

cat("\nAverage number of cases between 35-44: \n\n")

print(mean(esoph$ncases[16:30]))

cat("\nAverage number of cases between 45-54: \n\n")

print(mean(esoph$ncases[31:46]))

cat("\nAverage number of cases between 55-64: \n\n")

print(mean(esoph$ncases[47:63]))

cat("\nAverage number of cases between 65-74: \n\n")

print(mean(esoph$ncases[64:79]))

cat("\nAverage number of cases over 75: \n\n")

print(mean(esoph$ncases[80:88]))

boxplot(esoph$ncases ~ esoph$agegp, main="Esoph by age", border="gray", lwd=1, col=rainbow(5))
boxplot(esoph$ncases ~ esoph$alcgp, main="Esoph by alcohol", border="gray", lwd=1, col=rainbow(5))
boxplot(esoph$ncases ~ esoph$tobgp, main="Esophby tabacco", border="gray", lwd=1, col=rainbow(5))
