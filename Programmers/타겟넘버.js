function solution(numbers, target) {
  let answer = 0;
  let v = 0;
  let index = 0;
  function dfs(v, index) {
    if (index === numbers.length) {
      if (v === target) {
        answer += 1;
      }
    } else {
      dfs(v - numbers[index], index + 1);
      dfs(v + numbers[index], index + 1);
    }
  }
  dfs(0, index);
  return answer;
}
