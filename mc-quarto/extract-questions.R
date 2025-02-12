# Specify the input and output file names
input_file  <- "mc-quarto/answers-w1.qmd"
output_file <- "mc-quarto/questions-w1.qmd"

# Read the entire file as a single string
file_size <- file.info(input_file)$size
content   <- readChar(input_file, file_size)

# Split the content into slides.
# We assume that each slide is separated by a line containing exactly '---'
slides <- unlist(strsplit(content, "\n---\n"))

# Remove any slide that contains the phrase "## Answer to Question"
filtered_slides <- slides[ !grepl("## Answer to Question", slides) ]

# Reassemble the slides using the slide separator
new_content <- paste(filtered_slides, collapse = "\n---\n")

# Write the cleaned content to a new file
writeLines(new_content, output_file)

cat("New file created without answer slides:", output_file, "\n")
