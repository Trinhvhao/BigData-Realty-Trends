# Cài đặt và tải các thư viện cần thiết
library(sparklyr)
library(dplyr)
library(tidyr)
library(ggplot2)

# Kết nối Spark
sc <- spark_connect(master = "local")

# Đọc dữ liệu từ HDFS
df_2 <- spark_read_text(sc,
                        name = "bigdata_output_function",
                        path = "hdfs://localhost:9000/bigdata/output_function_2/part-00000")

# Chuyển dữ liệu từ Spark về dataframe trong R
df_local <- df_2 %>%
  collect() %>%  # Chuyển dữ liệu về local
  filter(nchar(line) > 0)  # Loại bỏ dòng trống nếu có

# Tách dữ liệu thành hai cột: House_Type và Count bằng cách sử dụng dấu tab "\t"
df_cleaned <- df_local %>%
  separate(line, into = c("House_Type", "Count"), sep = "\t") %>%
  mutate(Count = as.numeric(Count))  # Chuyển Count thành kiểu số

# Kiểm tra dữ liệu đã được tách
print(df_cleaned)

# Trực quan hóa bằng biểu đồ cột dọc
ggplot(df_cleaned, aes(x = House_Type, y = Count, fill = House_Type)) +
  geom_col() +
  labs(title = "Số lượng các loại nhà", x = "Loại nhà", y = "Số lượng") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))  # Xoay nhãn trục X để dễ đọc

