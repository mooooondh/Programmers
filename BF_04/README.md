피보나치 수
=====================
출처: https://programmers.co.kr/learn/courses/30/lessons/12945

<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다. </p>

<p>예를들어 </p>

<ul>
<li>F(2) = F(0) + F(1) = 0 + 1 = 1</li>
<li>F(3) = F(1) + F(2) = 1 + 1 = 2</li>
<li>F(4) = F(2) + F(3) = 1 + 2 = 3</li>
<li>F(5) = F(3) + F(4) = 2 + 3 = 5</li>
</ul>

<p>와 같이 이어집니다.</p>

<p>2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.</p>

<h5>제한 사항</h5>

<p>*&nbsp;n은 1이상, 100000이하인 자연수입니다.</p>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>3</td>
<td>2</td>
</tr>
<tr>
<td>5</td>
<td>5</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>피보나치수는 0번째부터 0, 1, 1, 2, 3, 5, ... 와 같이 이어집니다.</p>
</div>
    </div>