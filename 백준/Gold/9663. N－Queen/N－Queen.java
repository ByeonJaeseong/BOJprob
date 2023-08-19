import java.io.IOException;

import java.util.Arrays;

import java.util.Scanner;

 

public class Main {

    static int N, answer=0;

    

    public static void main(String [] args) throws IOException{

        int arr[];

        

        Scanner scan= new Scanner(System.in);

        N= scan.nextInt();

        arr= new int[N];

        

        for(int i=0; i<N; i++) {

            arr[0]=i;

            func(arr, 1);

        }

        System.out.println(answer);

        

    }

    

    public static void func(int[] arr, int index) {

        boolean isAnswer;

        if(index==N) {     //index 끝까지 도착했으면 answer++ 로 카운팅 해줌

            answer++;

            return;

        }

        for(int i=0; i<N; i++) {

            isAnswer=true;

            arr[index]=i;

            for(int j=0; j<index; j++) {     //arr[j]는 앞의 열의 값을 나타냄, i는 arr[index]

                if(arr[j]==i)isAnswer=false;     //같은 행에 놓였는지 체크

                if(Math.abs(arr[j]-i)==Math.abs(j-index))isAnswer=false;    //대각선에 놓였는지 체크

                if(!isAnswer) {   //같은 행이나 대각선에 놓인 경우 break

                    break;

                }

            }

            if(isAnswer) {     //올바른 위치일 경우 다음 index값 찾으러 출발

                func(arr, index+1);

            }

        }

    }//end func

}