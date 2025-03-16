# Tải các thư viện cần thiết
library(sparklyr)
library(dplyr)
library(tidyr)
library(ggplot2)

# Kết nối đến Spark
sc <- spark_connect(master = "local")

# Đọc dữ liệu từ HDFS
df_3 <- spark_read_text(sc,
                        name = "bigdata_output_function_3",
                        path = "hdfs://localhost:9000/bigdata/output_function_3/part-00000")

# Kiểm tra tên cột trong df_3
colnames(df_3)

# Tạo cột Area_Price từ cột chứa dữ liệu
df_3 <- df_3 %>%
  mutate(Area_Price = `line`) %>%  # Giả sử tên cột là `line`
  separate(Area_Price, into = c("Area", "Price"), sep = ", ") %>%
  mutate(
    Area = as.numeric(gsub("Area: ", "", Area)),
    Price = as.numeric(gsub("Price: ", "", Price))
  )

# Kiểm tra kết quả sau khi tách cột
head(df_3)

# Chuyển dữ liệu về local để vẽ đồ thị
df_3_local <- df_3 %>% collect()

# Vẽ biểu đồ phân tán với màu sắc
ggplot(df_3_local, aes(x = Area, y = Price, color = Price)) +
  geom_point(size = 3, alpha = 0.8) +  # Điều chỉnh kích thước và độ trong suốt
  scale_color_gradient(low = "blue", high = "red") +  # Chuyển màu từ xanh sang đỏ
  labs(title = "Scatter Plot of Area vs Price",
       x = "Area (sq meters)",
       y = "Price (USD)",
       color = "Price") +
  theme_minimal()
