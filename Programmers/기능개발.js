function solution(progresses, speeds) {
  let answer = [];
  let day = 0;
  let complete = 0;
  while (progresses.length) {
    if (progresses[0] + speeds[0] * day >= 100) {
      console.log(
        `오늘은 ${day}일이고 ${progresses[0]}  ${speeds[0]}가 제거됨`
      );
      complete += 1;
      progresses.shift();
      speeds.shift();
    } else {
      if (complete > 0) {
        answer.push(complete);
        complete = 0;
      }
      day += 1;
    }
  }
  if (complete) {
    answer.push(complete);
  }
  return answer;
}
