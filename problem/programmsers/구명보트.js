function solution(p, limit) {
  var answer = 0;
  p.sort((a, b) => {
    return a - b;
  });
  var j = p.length - 1;
  var i = 0;

  while (i <= j) {
    answer++;
    if (p[j] + p[i] <= limit) {
      i++;
    }
    j -= 1;
  }
  return answer;
}
