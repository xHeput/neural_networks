# neural_networks

Zestaw Pytań - 1
1.	Jakie jest zastosowanie warstwy dropout w sieciach neuronowych?
o	a) Zwiększenie liczby warstw w sieci.
o	b) Optymalizacja prędkości trenowania.
o	c) Redukcja przetrenowania poprzez wyłączanie losowych neuronów podczas treningu.
o	d) Redukcja wymiaru danych.
o	Odpowiedź: c
2.	Co to jest 'vanishing gradient problem' i jak wpływa na trenowanie głębokich sieci neuronowych?
o	a) Problem związany z przeuczeniem modelu.
o	b) Problem z nadmiernym wzrostem gradientów, co prowadzi do niestabilności sieci.
o	c) Problem zanikających gradientów, który powoduje trudności w trenowaniu głębokich sieci z powodu bardzo małych wartości gradientów.
o	d) Problem z utratą danych wejściowych w sieci neuronowej.
o	Odpowiedź: c
3.	Jakie techniki można zastosować do rozwiązania problemu vanishing gradient?
o	a) Zwiększenie liczby neuronów.
o	b) Użycie funkcji aktywacji ReLU, normalizacja batchowa, skrócone połączenia (residual connections).
o	c) Redukcja liczby warstw.
o	d) Użycie funkcji aktywacji sigmoid w każdej warstwie.
o	Odpowiedź: b
4.	Czym różni się GRU od LSTM?
o	a) LSTM jest prostsze w implementacji.
o	b) GRU nie ma oddzielnej komórki pamięci, ale integruje mechanizmy bramkowe w jednej bramie.
o	c) GRU ma więcej parametrów niż LSTM.
o	d) GRU jest mniej efektywne w przetwarzaniu sekwencji czasowych.
o	Odpowiedź: b
5.	W jaki sposób warstwa konwolucyjna przetwarza dane wejściowe?
o	a) Przetwarza dane równolegle w wielu warstwach w pełni połączonych.
o	b) Skalowaniem danych wejściowych do mniejszych wymiarów.
o	c) Usuwaniem szumów z danych wejściowych.
o	d) Aplikuje filtry (kernels) na dane wejściowe, generując mapy cech.
o	Odpowiedź: d
6.	Jaki jest wpływ liczby filtrów w warstwie konwolucyjnej na model?
o	a) Więcej filtrów zmniejsza ilość danych wyjściowych.
o	b) Więcej filtrów nie ma wpływu na model.
o	c) Więcej filtrów pozwala na wykrycie bardziej złożonych cech, ale zwiększa liczbę parametrów i złożoność obliczeniową.
o	d) Więcej filtrów zawsze poprawia wydajność modelu.
o	Odpowiedź: c
7.	Dlaczego normalizacja batchowa (Batch Normalization) jest stosowana w sieciach neuronowych?
o	a) Zmniejsza liczbę warstw w sieci.
o	b) Zwiększa rozdzielczość obrazów wejściowych.
o	c) Przyspiesza trenowanie i stabilizuje proces uczenia się.
o	d) Zwiększa liczbę neuronów w warstwie.
o	Odpowiedź: c
8.	Jaki jest główny cel stosowania algorytmu Sobela?
o	a) Segmentacja obrazów.
o	b) Wykrywanie krawędzi w obrazach.
o	c) Redukcja szumów.
o	d) Normalizacja obrazów.
o	Odpowiedź: b
9.	Jak działa mechanizm bramkowy w LSTM?
o	a) Agreguje informacje z poprzednich warstw.
o	b) Normalizuje dane wejściowe.
o	c) Wykonuje transformację cech.
o	d) Kontroluje przepływ informacji poprzez bramy wejścia, zapominania i wyjścia.
o	Odpowiedź: d
10.	Jak działa optymalizacja przy użyciu algorytmu Adam?
o	a) Redukuje wymiary danych wejściowych.
o	b) Skalibrowuje dane wyjściowe sieci neuronowej.
o	c) Łączy zalety Adagrad i RMSprop, dynamicznie dostosowując learning rate dla każdego parametru.
o	d) Używa stałego learning rate.
o	Odpowiedź: c
11.	Dlaczego używa się funkcji aktywacji ReLU w głębokich sieciach neuronowych?
o	a) Zwiększa liczbę neuronów.
o	b) Umożliwia wykrywanie krawędzi.
o	c) Przyspiesza obliczenia i redukuje problem zanikania gradientów.
o	d) Normalizuje dane wejściowe.
o	Odpowiedź: c
12.	Czym jest funkcja straty (loss function) w kontekście trenowania sieci neuronowych?
o	a) Algorytm do aktualizacji wag.
o	b) Metoda redukcji wymiarów danych.
o	c) Miara błędu między przewidywaniami modelu a rzeczywistymi wartościami.
o	d) Parametr kontrolujący wielkość kroków podczas optymalizacji.
o	Odpowiedź: c
13.	Jaki jest wpływ użycia większej liczby epok na trenowanie sieci neuronowej?
o	a) Zawsze poprawia dokładność modelu.
o	b) Może poprawić dokładność modelu, ale zwiększa ryzyko przeuczenia.
o	c) Zmniejsza ryzyko przeuczenia.
o	d) Nie ma wpływu na dokładność modelu.
o	Odpowiedź: b
14.	Czym różni się sieć jednowarstwowa od wielowarstwowej perceptronowej (MLP)?
o	a) MLP ma mniej parametrów.
o	b) Sieć jednowarstwowa jest bardziej złożona.
o	c) Sieć jednowarstwowa ma tylko jedną warstwę wyjściową, podczas gdy MLP ma wiele warstw ukrytych.
o	d) Sieć jednowarstwowa używa ReLU, a MLP nie.
o	Odpowiedź: c
15.	Jak działa funkcja aktywacji Softmax?
o	a) Redukuje wymiary danych wejściowych.
o	b) Umożliwia wykrywanie krawędzi.
o	c) Przekształca wyjścia sieci w prawdopodobieństwa.
o	d) Normalizuje dane wejściowe.
o	Odpowiedź: c
16.	Czym jest eksplozja gradientów i jak można ją kontrolować?
o	a) Problem z małymi gradientami, kontrolowany przez funkcję aktywacji ReLU.
o	b) Zjawisko, gdzie gradienty stają się zbyt duże podczas trenowania, kontrolowane przez normalizację gradientów.
o	c) Problem z utratą danych wejściowych, kontrolowany przez dropout.
o	d) Problem z przeuczeniem, kontrolowany przez regularizację.
o	Odpowiedź: b
17.	Jakie są zalety stosowania warstwy konwolucyjnej w sieciach neuronowych?
o	a) Zwiększenie liczby neuronów w warstwie.
o	b) Efektywne wykrywanie wzorców w danych przestrzennych, redukcja liczby parametrów.
o	c) Przyspieszenie trenowania.
o	d) Redukcja szumów w danych wejściowych.
o	Odpowiedź: b
18.	Jak działa mechanizm bramkowy w GRU?
o	a) Używa oddzielnych komórek pamięci.
o	b) Łączy funkcje bramy zapominania i bramy wejścia w jedną bramę, co upraszcza model.
o	c) Skalowuje dane wejściowe.
o	d) Wykonuje normalizację danych.
o	Odpowiedź: b
19.	Jaki jest wpływ regularyzacji L2 na trenowanie sieci neuronowej?
o	a) Przyspiesza trenowanie.
o	b) Redukuje liczbę neuronów w warstwie.
o	c) Dodaje karę za duże wartości wag, co pomaga w redukcji przetrenowania.
o	d) Zwiększa rozdzielczość obrazów wejściowych.
o	Odpowiedź: c
Zestaw Pytań - 2
1.	Jakie są zalety użycia funkcji aktywacji tanh w porównaniu do sigmoid?
o	a) tanh zawsze działa szybciej.
o	b) tanh ma wartości od -1 do 1, co daje średnie zero, co przyspiesza zbieżność.
o	c) tanh jest bardziej złożona w implementacji.
o	d) tanh zmniejsza liczbę neuronów.
o	Odpowiedź: b
2.	Jakie jest znaczenie parametrów 'forget gate' w LSTM?
o	a) Skalowanie danych wejściowych.
o	b) Kontrola informacji, które mają być zapomniane w komórce pamięci.
o	c) Normalizacja gradientów.
o	d) Wzmacnianie gradientów.
o	Odpowiedź: b
3.	W jaki sposób algorytm RMSprop różni się od SGD?
o	a) RMSprop używa średniej kwadratowej gradientów, aby dostosować learning rate.
o	b) RMSprop zawsze używa stałego learning rate.
o	c) RMSprop jest wolniejszy niż SGD.
o	d) RMSprop zmniejsza liczbę neuronów.
o	Odpowiedź: a
4.	Czym jest 'exploding gradient problem' i jak wpływa na trenowanie sieci?
o	a) Problem z małymi gradientami.
o	b) Gradienty stają się zbyt duże, powodując niestabilność i trudności w trenowaniu.
o	c) Problem z utratą danych wejściowych.
o	d) Problem z przeuczeniem.
o	Odpowiedź: b
5.	Dlaczego używa się funkcji aktywacji Leaky ReLU zamiast ReLU?
o	a) Leaky ReLU jest prostsza w implementacji.
o	b) Leaky ReLU pozwala na przepływ niewielkiej ilości ujemnych wartości, co zapobiega martwym neuronów.
o	c) Leaky ReLU zwiększa liczba warstw.
o	d) Leaky ReLU normalizuje dane wejściowe.
o	Odpowiedź: b
6.	Jaki jest główny cel użycia pooling layers w CNN?
o	a) Zwiększenie liczby parametrów.
o	b) Redukcja wymiarów i ilości danych, co zwiększa efektywność obliczeń.
o	c) Skalowanie danych wejściowych.
o	d) Normalizacja gradientów.
o	Odpowiedź: b
7.	Jak działa mechanizm atencji (attention) w sieciach neuronowych?
o	a) Skalowanie danych wejściowych.
o	b) Przypisywanie wag różnym częściom danych wejściowych, pozwalając modelowi skupić się na ważnych informacjach.
o	c) Normalizacja gradientów.
o	d) Redukcja wymiarów danych.
o	Odpowiedź: b
8.	Czym jest 'gradient clipping' i kiedy się go stosuje?
o	a) Skalowanie danych wejściowych.
o	b) Normalizacja gradientów.
o	c) Ograniczanie wartości gradientów, aby zapobiec eksplozji gradientów.
o	d) Zwiększanie liczby warstw.
o	Odpowiedź: c
9.	Jakie są zalety użycia architektury ResNet?
o	a) Prostsza implementacja.
o	b) Umożliwia trenowanie bardzo głębokich sieci poprzez skrócone połączenia (residual connections).
o	c) Redukcja liczby warstw.
o	d) Normalizacja danych wejściowych.
o	Odpowiedź: b
10.	Dlaczego używa się warstwy normalizacji (Layer Normalization) w sieciach neuronowych?
o	a) Skalowanie danych wejściowych.
o	b) Normalizacja gradientów.
o	c) Stabilizuje proces uczenia, normalizując aktywacje w poprzek poszczególnych warstw.
o	d) Zwiększanie liczby warstw.
o	Odpowiedź: c
11.	Jak działa mechanizm 'skip connections' w architekturach sieci neuronowych?
o	a) Przetwarza dane równolegle.
o	b) Dodaje bezpośrednie połączenia pomiędzy odległymi warstwami, ułatwiając przepływ gradientów.
o	c) Skalowanie danych wejściowych.
o	d) Redukcja liczby warstw.
o	Odpowiedź: b
12.	Jakie są zalety użycia warstwy konwolucyjnej o głębokich filtrach (Deep Convolutional Layer)?
o	a) Zwiększenie liczby neuronów.
o	b) Skalowanie danych wejściowych.
o	c) Wykrywanie bardziej złożonych cech i wzorców w danych.
o	d) Redukcja szumów.
o	Odpowiedź: c
13.	Jak działa mechanizm 'attention' w kontekście przetwarzania sekwencji czasowych?
o	a) Skalowanie danych wejściowych.
o	b) Przypisywanie dynamicznych wag różnym częściom sekwencji, aby skupić się na ważnych elementach.
o	c) Redukcja liczby warstw.
o	d) Normalizacja gradientów.
o	Odpowiedź: b
14.	Czym jest funkcja kosztu (cost function) w trenowaniu sieci neuronowych?
o	a) Algorytm do aktualizacji wag.
o	b) Miara błędu między przewidywaniami modelu a rzeczywistymi wartościami.
o	c) Metoda redukcji wymiarów danych.
o	d) Parametr kontrolujący wielkość kroków podczas optymalizacji.
o	Odpowiedź: b
15.	Jakie są zalety użycia architektury GAN (Generative Adversarial Network)?
o	a) Skalowanie danych wejściowych.
o	b) Generowanie realistycznych danych, np. obrazów, poprzez rywalizację dwóch sieci.
o	c) Normalizacja gradientów.
o	d) Redukcja liczby warstw.
o	Odpowiedź: b
16.	Jak działa mechanizm 'dropout' podczas testowania modelu?
o	a) Włącza losowo wybrane neurony.
o	b) Wyłącza losowo wybrane neurony.
o	c) Skalowanie danych wejściowych.
o	d) Włącza wszystkie neurony i skaluje wyjścia warstwy.
o	Odpowiedź: d
17.	Jakie są zalety użycia warstwy 'fully connected' w CNN?
o	a) Redukcja liczby parametrów.
o	b) Łączenie wszystkich neuronów poprzedniej warstwy z neuronami bieżącej warstwy, co pozwala na globalne przetwarzanie danych.
o	c) Skalowanie danych wejściowych.
o	d) Normalizacja gradientów.
o	Odpowiedź: b
18.	Czym jest 'weight decay' w kontekście regularyzacji?
o	a) Zwiększanie liczby neuronów.
o	b) Dodanie kar za duże wartości wag, co pomaga w redukcji przetrenowania.
o	c) Skalowanie danych wejściowych.
o	d) Normalizacja gradientów.
o	Odpowiedź: b
19.	Jak działa mechanizm 'attention' w sieciach Transformer?
o	a) Normalizacja danych wejściowych.
o	b) Przypisywanie dynamicznych wag różnym częściom wejścia, umożliwiając modelowi zwracanie uwagi na różne aspekty danych.
o	c) Redukcja liczby warstw.
o	d) Skalowanie danych wejściowych.
o	Odpowiedź: b
20.	Jakie są zalety użycia warstwy 'dense' w sieciach neuronowych?
o	a) Redukcja liczby neuronów.
o	b) Łączenie każdego neuronu z każdym neuronem w warstwie następnej, co umożliwia pełne przetwarzanie danych.
o	c) Skalowanie danych wejściowych.
o	d) Normalizacja gradientów.
o	Odpowiedź: b

