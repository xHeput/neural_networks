# neural_networks

Zestaw Pytań - 1

    Jakie jest zastosowanie warstwy dropout w sieciach neuronowych?
        a) Zwiększenie liczby warstw w sieci.
        b) Optymalizacja prędkości trenowania.
        c) Redukcja przetrenowania poprzez wyłączanie losowych neuronów podczas treningu.
        d) Redukcja wymiaru danych.
        Odpowiedź: c

    Co to jest 'vanishing gradient problem' i jak wpływa na trenowanie głębokich sieci neuronowych?
        a) Problem związany z przeuczeniem modelu.
        b) Problem z nadmiernym wzrostem gradientów, co prowadzi do niestabilności sieci.
        c) Problem zanikających gradientów, który powoduje trudności w trenowaniu głębokich sieci z powodu bardzo małych wartości gradientów.
        d) Problem z utratą danych wejściowych w sieci neuronowej.
        Odpowiedź: c

    Jakie techniki można zastosować do rozwiązania problemu vanishing gradient?
        a) Zwiększenie liczby neuronów.
        b) Użycie funkcji aktywacji ReLU, normalizacja batchowa, skrócone połączenia (residual connections).
        c) Redukcja liczby warstw.
        d) Użycie funkcji aktywacji sigmoid w każdej warstwie.
        Odpowiedź: b

    Czym różni się GRU od LSTM?
        a) LSTM jest prostsze w implementacji.
        b) GRU nie ma oddzielnej komórki pamięci, ale integruje mechanizmy bramkowe w jednej bramie.
        c) GRU ma więcej parametrów niż LSTM.
        d) GRU jest mniej efektywne w przetwarzaniu sekwencji czasowych.
        Odpowiedź: b

    W jaki sposób warstwa konwolucyjna przetwarza dane wejściowe?
        a) Przetwarza dane równolegle w wielu warstwach w pełni połączonych.
        b) Skalowaniem danych wejściowych do mniejszych wymiarów.
        c) Usuwaniem szumów z danych wejściowych.
        d) Aplikuje filtry (kernels) na dane wejściowe, generując mapy cech.
        Odpowiedź: d

    Jaki jest wpływ liczby filtrów w warstwie konwolucyjnej na model?
        a) Więcej filtrów zmniejsza ilość danych wyjściowych.
        b) Więcej filtrów nie ma wpływu na model.
        c) Więcej filtrów pozwala na wykrycie bardziej złożonych cech, ale zwiększa liczbę parametrów i złożoność obliczeniową.
        d) Więcej filtrów zawsze poprawia wydajność modelu.
        Odpowiedź: c

    Dlaczego normalizacja batchowa (Batch Normalization) jest stosowana w sieciach neuronowych?
        a) Zmniejsza liczbę warstw w sieci.
        b) Zwiększa rozdzielczość obrazów wejściowych.
        c) Przyspiesza trenowanie i stabilizuje proces uczenia się.
        d) Zwiększa liczbę neuronów w warstwie.
        Odpowiedź: c

    Jaki jest główny cel stosowania algorytmu Sobela?
        a) Segmentacja obrazów.
        b) Wykrywanie krawędzi w obrazach.
        c) Redukcja szumów.
        d) Normalizacja obrazów.
        Odpowiedź: b

    Jak działa mechanizm bramkowy w LSTM?
        a) Agreguje informacje z poprzednich warstw.
        b) Normalizuje dane wejściowe.
        c) Wykonuje transformację cech.
        d) Kontroluje przepływ informacji poprzez bramy wejścia, zapominania i wyjścia.
        Odpowiedź: d

    Jak działa optymalizacja przy użyciu algorytmu Adam?
        a) Redukuje wymiary danych wejściowych.
        b) Skalibrowuje dane wyjściowe sieci neuronowej.
        c) Łączy zalety Adagrad i RMSprop, dynamicznie dostosowując learning rate dla każdego parametru.
        d) Używa stałego learning rate.
        Odpowiedź: c

    Dlaczego używa się funkcji aktywacji ReLU w głębokich sieciach neuronowych?
        a) Zwiększa liczbę neuronów.
        b) Umożliwia wykrywanie krawędzi.
        c) Przyspiesza obliczenia i redukuje problem zanikania gradientów.
        d) Normalizuje dane wejściowe.
        Odpowiedź: c

    Czym jest funkcja straty (loss function) w kontekście trenowania sieci neuronowych?
        a) Algorytm do aktualizacji wag.
        b) Metoda redukcji wymiarów danych.
        c) Miara błędu między przewidywaniami modelu a rzeczywistymi wartościami.
        d) Parametr kontrolujący wielkość kroków podczas optymalizacji.
        Odpowiedź: c

    Jaki jest wpływ użycia większej liczby epok na trenowanie sieci neuronowej?
        a) Zawsze poprawia dokładność modelu.
        b) Może poprawić dokładność modelu, ale zwiększa ryzyko przeuczenia.
        c) Zmniejsza ryzyko przeuczenia.
        d) Nie ma wpływu na dokładność modelu.
        Odpowiedź: b

    Czym różni się sieć jednowarstwowa od wielowarstwowej perceptronowej (MLP)?
        a) MLP ma mniej parametrów.
        b) Sieć jednowarstwowa jest bardziej złożona.
        c) Sieć jednowarstwowa ma tylko jedną warstwę wyjściową, podczas gdy MLP ma wiele warstw ukrytych.
        d) Sieć jednowarstwowa używa ReLU, a MLP nie.
        Odpowiedź: c

    Jak działa funkcja aktywacji Softmax?
        a) Redukuje wymiary danych wejściowych.
        b) Umożliwia wykrywanie krawędzi.
        c) Przekształca wyjścia sieci w prawdopodobieństwa.
        d) Normalizuje dane wejściowe.
        Odpowiedź: c

    Czym jest eksplozja gradientów i jak można ją kontrolować?
        a) Problem z małymi gradientami, kontrolowany przez funkcję aktywacji ReLU.
        b) Zjawisko, gdzie gradienty stają się zbyt duże podczas trenowania, kontrolowane przez normalizację gradientów.
        c) Problem z utratą danych wejściowych, kontrolowany przez dropout.
        d) Problem z przeuczeniem, kontrolowany przez regularizację.
        Odpowiedź: b

    Jakie są zalety stosowania warstwy konwolucyjnej w sieciach neuronowych?
        a) Zwiększenie liczby neuronów w warstwie.
        b) Efektywne wykrywanie wzorców w danych przestrzennych, redukcja liczby parametrów.
        c) Przyspieszenie trenowania.
        d) Redukcja szumów w danych wejściowych.
        Odpowiedź: b

    Jak działa mechanizm bramkowy w GRU?
        a) Używa oddzielnych komórek pamięci.
        b) Łączy funkcje bramy zapominania i bramy wejścia w jedną bramę, co upraszcza model.
        c) Skalowuje dane wejściowe.
        d) Wykonuje normalizację danych.
        Odpowiedź: b

    Jaki jest wpływ regularyzacji L2 na trenowanie sieci neuronowej?
        a) Przyspiesza trenowanie.
        b) Redukuje liczbę neuronów w warstwie.
        c) Dodaje karę za duże wartości wag, co pomaga w redukcji przetrenowania.
        d) Zwiększa rozdzielczość obrazów wejściowych.
        Odpowiedź: c
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

