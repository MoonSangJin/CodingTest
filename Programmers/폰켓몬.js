function solution(nums) {
  let answer = 0;
  let answer_length = nums.length / 2;
  let set = new Set(nums);
  let number = [...set];
  if (number.length > answer_length) {
    answer = answer_length;
  } else {
    answer = number.length;
  }
  return answer;
}
