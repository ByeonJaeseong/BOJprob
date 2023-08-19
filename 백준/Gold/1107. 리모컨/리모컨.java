import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class Main {
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str = br.readLine();
    int input = Integer.parseInt(str);
    TreeSet<Integer> ts = new TreeSet<Integer>();
    /*
     * int digit = str.length();
     * String[] strArray = str.trim().split("");
     * int[] inputNum = new int[6];
     * TreeSet ts = new TreeSet<Integer>();
     * 
     * for (int i = 6-digit; i < digit; i++) {
     * inputNum[i] = Integer.parseInt(strArray[i]);
     * }
     */
    int M = Integer.parseInt(br.readLine()); // 버튼개수
  
    // 버튼이 0인 경우를 고려해서 코드짜야할듯
    if (M != 0) {
    str = br.readLine();
    String[] strArray = str.trim().split(" ");
      int[] givenNum = new int[strArray.length];
      for (int i = 0; i < strArray.length; i++) {
        givenNum[i] = Integer.parseInt(strArray[i]);
      }
      for (int i = 0; i <= 1000000; i++) {
        if (i != 0) {
          int data = i;
          String data2 = String.valueOf(data);
          finder: while (data != 0) {
            int residue = data % 10;
            for (int j = 0; j < givenNum.length; j++) {
              if (residue == givenNum[j]) {
                break finder;
              }
            }
            data = data / 10;
          }
          if (data == 0) {
            ts.add(Math.abs(input - i) + data2.length());
          }
        } else {
          boolean mark = false;
          for (int j = 0; j < givenNum.length; j++) {
            if (givenNum[j] == 0)
              mark = true;
          }
          if (!mark) {
            ts.add(input + 1);
          }
        }
      }
    } else {
      ts.add(String.valueOf(input).length());
    }
    ts.add(Math.abs(input - 100));
    System.out.println(ts.pollFirst());

    /*
     * for(int i=0; i<10; i++){
     * boolean mark = true;
     * for(int j=0; j<givenNum.length; j++){
     * if(i==givenNum[j]){
     * mark = false;
     * break;
     * }
     * }
     * if(mark){
     * list.add(i);
     * }
     * }
     */

  }
}