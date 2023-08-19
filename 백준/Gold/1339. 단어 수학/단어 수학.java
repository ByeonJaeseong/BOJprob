import java.io.*;
import java.util.*;

class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String input = br.readLine();
    int N = Integer.parseInt(input);
    String[][] inputStr = new String[N][8];
    for(int i=0; i<N; i++){
      
    }
    Set<String> set = new HashSet<String>();
    int Max =0;
    for(int i=0; i<N; i++){
      input = br.readLine();
      String[] inputArr= input.trim().split("");
      if(Max<inputArr.length)
        Max=inputArr.length;
      for(int j=0; j<inputArr.length; j++){
        inputStr[i][7-j]=inputArr[inputArr.length-j-1];
      }
    }
    // 얘가 최대 8-Max
    for(int i=0; i<N; i++){
      for(int j=0; j<8; j++){
        if(inputStr[i][j]!=null)
          set.add(inputStr[i][j]);
      } 
    }
    int[] number = new int[set.size()];
    int num=0;
    for(String s : set){
      for(int i=0; i<N; i++){
        for(int j=0; j<8; j++){
          if(s.equals(inputStr[i][j])){
            switch(j){
              case 7:
                number[num]+=1;
                break;
              case 6:
                number[num]+=10;
                break;
              case 5:
                number[num]+=100;
                break;
              case 4:
                number[num]+=1000;
                break;
              case 3:
                number[num]+=10000;
                break;
              case 2:
                number[num]+=100000;
                break;
              case 1:
                number[num]+=1000000;
                break;
              case 0:
                number[num]+=10000000;
                break;
            }
          }
        }
      }
      num++;
    }   
    ArrayList<Integer> list = new ArrayList<Integer>();

    for(int i=0; i<number.length; i++)
      list.add(number[i]);
    Collections.sort(list);
    
    int result =0;
    int j=0;
    for(int i=9-number.length+1; i<=9; i++){
     // System.out.println(list.get(j));
      result=result+list.get(j)*i;
      j++;
    }
    System.out.println(result);


  }
}