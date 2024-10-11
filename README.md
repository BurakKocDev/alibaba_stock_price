# alibaba_stock_price
 stock price predict
English Summary
This Python script performs comprehensive analysis and prediction of Alibaba's (BABA) stock prices using historical data. Here's a breakdown of its functionalities:

Data Loading and Exploration:

Loading Data: The script reads the BABA.CSV file containing Alibaba's stock data.
Initial Inspection: It displays the first five rows, column names, dataset shape, and checks for missing values.
Data Types and Missing Values: It prints the number of missing values per column and their data types.
Date Conversion: The Date column is converted to a datetime format for easier manipulation.
Descriptive Statistics: Basic statistical measures of the dataset are computed and displayed.
Data Visualization:

Stock Prices Plot: Visualizes Open, High, Low, and Close prices over time.
Adjusted Close Price Plot: Shows the Adj Close price, accounting for corporate actions.
Trading Volume Plot: Displays the trading volume using a bar chart.
Moving Averages:
30-Day and 90-Day Moving Averages: Calculates and plots these averages alongside the Close price to identify trends.
Specific Period Analysis (First Half of 2020): Focuses on Alibaba's stock performance during the initial months of the COVID-19 pandemic.
Daily Percentage Change Distribution: Plots a histogram to illustrate the volatility of daily price changes.
XGBoost Regression Model for Price Prediction:

Feature Selection: Chooses relevant features (Open, High, Low, Volume, Adj Close) to predict the Close price.
Data Splitting: Divides the dataset into training (80%) and testing (20%) sets.
Model Initialization and Training:
Initializes the XGBRegressor with specific parameters.
Trains the model on the training data.
Prediction and Evaluation:
Predicts Close prices on the test set.
Calculates performance metrics: Root Mean Squared Error (RMSE), Mean Absolute Percentage Error (MAPE), and R-squared (R²).
Visualization of Predictions:
Plots actual vs. predicted Close prices to assess model performance.
Results Explanation:

The visualizations provide insights into Alibaba's stock performance, highlighting trends, volatility, and the impact of significant events like the COVID-19 pandemic.
The XGBoost model demonstrates its ability to predict future Close prices with reasonable accuracy, as indicated by the calculated performance metrics.
The prediction plots show how closely the model's forecasts align with actual stock prices, offering a visual validation of its effectiveness.
Türkçe Özet
Bu Python betiği, Alibaba'nın (BABA) hisse senedi fiyatlarını geçmiş verilere dayanarak kapsamlı bir şekilde analiz eder ve tahmin eder. İşte işlevlerinin özeti:

Veri Yükleme ve Keşif:

Veri Yükleme: Betik, Alibaba'nın hisse verilerini içeren BABA.CSV dosyasını okur.
İlk İnceleme: İlk beş satırı, sütun isimlerini, veri setinin şeklini görüntüler ve eksik değerleri kontrol eder.
Veri Tipleri ve Eksik Değerler: Her sütundaki eksik değer sayısını ve veri tiplerini yazdırır.
Tarih Dönüşümü: Date sütunu, daha kolay manipülasyon için datetime formatına dönüştürülür.
Betimsel İstatistikler: Veri setinin temel istatistiksel ölçümleri hesaplanır ve görüntülenir.
Veri Görselleştirme:

Hisse Fiyatları Grafiği: Zaman içinde Open, High, Low ve Close fiyatlarını görselleştirir.
Düzeltilmiş Kapanış Fiyatı Grafiği: Kurumsal işlemleri hesaba katarak Adj Close fiyatını gösterir.
İşlem Hacmi Grafiği: İşlem hacmini bar grafiği ile gösterir.
Hareketli Ortalamalar:
30 Günlük ve 90 Günlük Hareketli Ortalamalar: Bu ortalamaları Close fiyatıyla birlikte hesaplar ve trendleri belirlemek için grafiğe ekler.
Belirli Dönem Analizi (2020 İlk Yarı): COVID-19 pandemisinin ilk aylarında Alibaba'nın hisse performansına odaklanır.
Günlük Yüzde Değişim Dağılımı: Günlük fiyat değişikliklerinin volatilitesini göstermek için histogram çizer.
Fiyat Tahmini İçin XGBoost Regresyon Modeli:

Özellik Seçimi: Open, High, Low, Volume, Adj Close gibi ilgili özellikleri seçerek Close fiyatını tahmin eder.
Veri Bölme: Veri setini %80 eğitim ve %20 test olarak ayırır.
Modelin Başlatılması ve Eğitimi:
Belirli parametrelerle XGBRegressor başlatılır.
Model, eğitim verisi üzerinde eğitilir.
Tahmin ve Değerlendirme:
Test setinde Close fiyatları tahmin edilir.
Performans metrikleri hesaplanır: Kök Ortalama Kare Hatası (RMSE), Ortalama Mutlak Yüzde Hatası (MAPE) ve R-kare (R²).
Tahminlerin Görselleştirilmesi:
Gerçek ve tahmin edilen Close fiyatlarını karşılaştıran grafikler çizilerek model performansı değerlendirilir.
Sonuçların Açıklanması:

Görselleştirmeler, Alibaba'nın hisse performansına dair trendler, volatilite ve COVID-19 pandemisi gibi önemli olayların etkilerini ortaya koyar.
XGBoost modeli, hesaplanan performans metrikleriyle gösterildiği üzere gelecekteki Close fiyatlarını makul bir doğrulukla tahmin etme yeteneğini sergiler.
Tahmin grafikleri, modelin tahminlerinin gerçek hisse fiyatlarıyla ne kadar uyumlu olduğunu görsel olarak göstererek etkinliğini doğrular.
