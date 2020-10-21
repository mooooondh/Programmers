수식 최대화
==================
https://programmers.co.kr/learn/courses/30/lessons/67257

<div class="guide-section" id="tour2" style="width: calc(40% - 12px);">
    <div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>IT 벤처 회사를 운영하고 있는 <code>라이언</code>은 매년 사내 해커톤 대회를 개최하여 우승자에게 상금을 지급하고 있습니다.<br>
이번 대회에서는 우승자에게 지급되는 상금을 이전 대회와는 다르게 다음과 같은 방식으로 결정하려고 합니다.<br>
해커톤 대회에 참가하는 모든 참가자들에게는 숫자들과 3가지의 연산문자(<code>+, -, *</code>) 만으로 이루어진 연산 수식이 전달되며, 참가자의 미션은 전달받은 수식에 포함된 연산자의 우선순위를 자유롭게 재정의하여 만들 수 있는 가장 큰 숫자를 제출하는 것입니다.<br>
단, 연산자의 우선순위를 새로 정의할 때, 같은 순위의 연산자는 없어야 합니다. 즉, <code>+</code> &gt; <code>-</code> &gt; <code>*</code> 또는 <code>-</code> &gt; <code>*</code> &gt; <code>+</code> 등과 같이 연산자 우선순위를 정의할 수 있으나 <code>+,*</code> &gt; <code>-</code> 또는 <code>*</code> &gt; <code>+,-</code>처럼 2개 이상의 연산자가 동일한 순위를 가지도록 연산자 우선순위를 정의할 수는 없습니다. 수식에 포함된 연산자가 2개라면 정의할 수 있는 연산자 우선순위 조합은 2! = 2가지이며, 연산자가 3개라면 3! = 6가지 조합이 가능합니다.<br>
만약 계산된 결과가 음수라면 해당 숫자의 절댓값으로 변환하여 제출하며 제출한 숫자가 가장 큰 참가자를 우승자로 선정하며, 우승자가 제출한 숫자를 우승상금으로 지급하게 됩니다.</p>

<p>예를 들어, 참가자 중 <code>네오</code>가 아래와 같은 수식을 전달받았다고 가정합니다.</p>

<p><code>"100-200*300-500+20"</code></p>

<p>일반적으로 수학 및 전산학에서 약속된 연산자 우선순위에 따르면 더하기와 빼기는 서로 동등하며 곱하기는 더하기, 빼기에 비해 우선순위가 높아 <code>*</code> &gt; <code>+,-</code> 로 우선순위가 정의되어 있습니다.<br>
대회 규칙에 따라 <code>+</code> &gt; <code>-</code> &gt; <code>*</code>  또는  <code>-</code> &gt; <code>*</code> &gt; <code>+</code> 등과 같이 연산자 우선순위를 정의할 수 있으나 <code>+,*</code> &gt; <code>-</code> 또는 <code>*</code> &gt; <code>+,-</code> 처럼 2개 이상의 연산자가 동일한 순위를 가지도록 연산자 우선순위를 정의할 수는 없습니다.<br>
수식에 연산자가 3개 주어졌으므로 가능한 연산자 우선순위 조합은 3! = 6가지이며, 그 중 <code>+</code> &gt; <code>-</code> &gt; <code>*</code> 로 연산자 우선순위를 정한다면 결괏값은 22,000원이 됩니다.<br>
반면에 <code>*</code> &gt; <code>+</code> &gt; <code>-</code> 로 연산자 우선순위를 정한다면 수식의 결괏값은 -60,420 이지만, 규칙에 따라 우승 시 상금은 절댓값인 60,420원이 됩니다.</p>

<p>참가자에게 주어진 연산 수식이 담긴 문자열 expression이 매개변수로 주어질 때, 우승 시 받을 수 있는 가장 큰 상금 금액을 return 하도록 solution 함수를 완성해주세요.</p>

<h5><strong>[제한사항]</strong></h5>

<ul>
<li>expression은 길이가 3 이상 100 이하인 문자열입니다.</li>
<li>expression은 공백문자, 괄호문자 없이 오로지 숫자와 3가지의 연산자(<code>+, -, *</code>) 만으로 이루어진 올바른 중위표기법(연산의 두 대상 사이에 연산기호를 사용하는 방식)으로 표현된 연산식입니다. 잘못된 연산식은 입력으로 주어지지 않습니다.

<ul>
<li>즉, <code>"402+-561*"</code>처럼 잘못된 수식은 올바른 중위표기법이 아니므로 주어지지 않습니다.<br></li>
</ul></li>
<li>expression의 피연산자(operand)는 0 이상 999 이하의 숫자입니다.

<ul>
<li>즉, <code>"100-2145*458+12"</code>처럼 999를 초과하는 피연산자가 포함된 수식은 입력으로 주어지지 않습니다.</li>
<li><code>"-56+100"</code>처럼 피연산자가 음수인 수식도 입력으로 주어지지 않습니다. </li>
</ul></li>
<li>expression은 적어도 1개 이상의 연산자를 포함하고 있습니다.</li>
<li>연산자 우선순위를 어떻게 적용하더라도, expression의 중간 계산값과 최종 결괏값은 절댓값이 2<sup>63</sup> - 1 이하가 되도록 입력이 주어집니다.</li>
<li>같은 연산자끼리는 앞에 있는 것의 우선순위가 더 높습니다.</li>
</ul>

<hr>

<h5><strong>입출력 예</strong></h5>
<table class="table">
        <thead><tr>
<th>expression</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td><code>"100-200*300-500+20"</code></td>
<td>60420</td>
</tr>
<tr>
<td><code>"50*6-3*2"</code></td>
<td>300</td>
</tr>
</tbody>
      </table>
<h5><strong>입출력 예에 대한 설명</strong></h5>

<p><strong>입출력 예 #1</strong><br>
<code>*</code> &gt; <code>+</code> &gt; <code>-</code> 로 연산자 우선순위를 정했을 때, 가장 큰 절댓값을 얻을 수 있습니다.<br>
연산 순서는 아래와 같습니다.<br>
<code>100-200*300-500+20</code><br>
= <code>100-(200*300)-500+20</code><br>
= <code>100-60000-(500+20)</code><br>
= <code>(100-60000)-520</code><br>
= <code>(-59900-520)</code><br>
= <code>-60420</code><br>
따라서, 우승 시 받을 수 있는 상금은 |-60420| = 60420 입니다.</p>

<p><strong>입출력 예 #2</strong><br>
<code>-</code> &gt; <code>*</code> 로 연산자 우선순위를 정했을 때, 가장 큰 절댓값을 얻을 수 있습니다.<br>
연산 순서는 아래와 같습니다.(expression에서 <code>+</code> 연산자는 나타나지 않았으므로, 고려할 필요가 없습니다.)<br>
<code>50*6-3*2</code><br>
= <code>50*(6-3)*2</code><br>
= <code>(50*3)*2</code><br>
= <code>150*2</code><br>
= <code>300</code><br>
따라서, 우승 시 받을 수 있는 상금은 300 입니다.</p>
</div>
    </div>

  </div>