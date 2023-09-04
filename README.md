# Основы вычислительной физики

Решение задач из курса по основам вычислительной физики.

---

<details>
<summary>
<b>Найти эпсилон (<a href="lesson_1/ulp.py">ulp.py</a>)</b>
</summary>

#### Условие

*Машинным* $\epsilon$ называется такое число, что 1 + $\epsilon/2 = 1$, но $1 + \epsilon \not ={1}$. (Также часто используется обозначение ULP - *unit in the last place*, или *unit of least precision*, единица в младшем разряде.) Найти машинное $\epsilon$, число разрядов в мантиссе, максимальную и минимальную степени, при вычислениях с обычной и двойной точностью. Сравнить друг с другом четыре числа: $1, 1 + \frac{\epsilon}{2},1+\epsilon,1+\epsilon+\frac{\epsilon}{2}$, объяснить результат. 

#### Указания

При использовании Python воспользуйтесь типами np.float32 и np.float64.

</details>

---

<details>
<summary>
<b>Решить уравнение (<a href="lesson_2/solve.py">solve.py</a>)</b>
</summary>

#### Условие

Используя методы дихотомии, простых итераций и Ньютона, найти уровень энергии $E$ основного состояния квантовой частицы в прямоугольной потенциальной яме

$$-\frac{1}{2}\psi''(x) + U(x)\psi(x)=E\psi(x), U(x)=\begin{cases}-U_0, |x| \leq a \\ 0, |x| \gt a\end{cases}$$


</details>

---

<details>
<summary>
<b>Вычислить интегралы (<a href="lesson_3/int.py">int.py</a>)</b>
</summary>

#### Условие

...

</details>

---

<details>
<summary>
<b>Вычислить производную (<a href="lesson_4/diff.py">int.py</a>)</b>
</summary>

#### Условие

...

</details>

---
