# 🎭 Gerçek Zamanlı Duygu Tespiti

Bu proje, yüz ifadelerinden duyguları tespit eden bir uygulamadır. Keras ile eğitilmiş bir Convolutional Neural Network (CNN) kullanarak duyguları sınıflandırır.

## 📋 İçindekiler
- [Özellikler](#özellikler)
- [Kullanım](#kullanım)
- [Veri Seti](#veri-seti)
- [Model Eğitimi](#model-eğitimi)
- [Sonuçlar](#sonuçlar)
- [Katkıda Bulunanlar](#katkıda-bulunanlar)

## ✨ Özellikler
- Gerçek zamanlı yüz tanıma ve duygu tespiti 📷
- Keras entegrasyonu 🧠

  
📊 Veri Seti
Bu proje, https://www.kaggle.com/datasets/jonathanoheix/face-expression-recognition-dataset veri setini kullanmaktadır. Veri seti, 48x48 piksel boyutunda gri tonlamalı yüz görüntülerinden oluşur ve aşağıdaki duygu kategorilerini içerir:

Mutlu 😊
Üzgün 😢
Sinirli 😡
Nötr 😐
🧠 Model Eğitimi
Model eğitimi, aşağıdaki adımları izleyerek gerçekleştirildi:

Veri ön işleme: Görüntülerin yeniden boyutlandırılması ve normalizasyonu.
Model mimarisi: CNN modelinin oluşturulması ve derlenmesi.
Model eğitimi: Modelin eğitilmesi ve doğrulanması.
📈 Sonuçlar
Modelin eğitim ve doğrulama sürecine ait bazı metrikler:

Epoch	Eğitim Doğruluğu	Eğitim Kaybı	Doğrulama Doğruluğu	Doğrulama Kaybı
1	0.3377	1.3725	0.3311	1.3616
20	0.6737	0.7968	0.6730	0.8090
👥 Katkıda Bulunanlar
Yasemin Başkaya - yasemin.baskaya19@gmail.com


Bu projeyi beğendiyseniz ⭐ vermeyi unutmayın!
