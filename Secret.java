/**
 * 프로그래머스 level1- 둘만의 암호
 * */

public class Secret {
    public static String solution(String s, String skip, int index) {
        String answer = "";
        for (int i = 0; i < s.length(); i++) { // s를 돌고
            // 현재 글자를 뽑기. 하지만 지금 문자열이니까 계산하기 편하게 숫자로 바꾸기 위해서 97빼기
            int current = s.charAt(i) - 97;
            // 총 카운팅되야할 수 즉 총 움직여야 할 수
            int count = 0;

            // while문에서 총 몇글자 움직일건지를 확인
            while (count < index) {
                // 한 칸씩 이동 후 그 이동한 문자열이 'z'보다 크면 다시 'a'로-> 모듈러연산자 사용
                current = (current + 1) % 26; // uvxyz

                // 찾은 숫자를 문자로 변환->contains함수 사용위해 문자를 다시 한번 더 문자열로 변환
                char currentChar = (char) (current + 97);
                String currentString = String.valueOf(currentChar);
                if (!skip.contains(currentString)) {
                    count++;
                }
            }
            char plusChar = (char) (current + 97);
            answer = answer + plusChar;
        }
        return answer;
    }

    public static void main(String[] args) {

        String s = "aukks";
        String skip = "wbqd";
        int index = 5;

        System.out.println(solution(s, skip, index));
    }
}
