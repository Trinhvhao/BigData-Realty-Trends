# Cài đặt và tải thư viện
library(sparklyr)
library(dplyr)
library(ggplot2)

# Kết nối Spark
sc <- spark_connect(master = "local")

# Đọc dữ liệu từ HDFS
df_1 <- spark_read_text(sc,
                        name = "bigdata_output_function_1",
                        path = "hdfs://localhost:9000/bigdata/output_function_1/part-00000")

# Chuyển dữ liệu về local
df_local <- df_1 %>%
  collect() %>%
  tidyr::separate(line, into = c("City", "Price"), sep = "\\t") %>%
  mutate(Price = as.numeric(Price))

# Vẽ biểu đồ cột
ggplot(df_local, aes(x = reorder(City, Price), y = Price, fill = City)) +
  geom_col() +
  coord_flip() +  # Xoay ngang để dễ đọc
  labs(title = "Giá trung bình của các thành phố", x = "Thành phố", y = "Giá ($)") +
  theme_minimal()

