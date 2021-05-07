function solution(numbers) {
  let str_numbers = numbers.map((i) => String(i));
  let answer = str_numbers
    .sort((a, b) => {
      return b + a - (a + b);
    })
    .join('');
  return answer[0] === '0' ? '0' : answer;
}
