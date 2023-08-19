import java.io.BufferedReader;
import java.io.InputStreamReader;

class Main {
  public static int[][] cityToCity;
  public static int[] totalPay;
  public static boolean[][] exist;
  public static boolean[] visitCity;
  public static void dijkstra(int[][] cityToCity, int[] totalPay, boolean[] visitCity, int start){
  // System.out.println(start);
    visitCity[start] = true;

    for(int i=0; i<visitCity.length; i++){
      if(!visitCity[i]/*최솟값이 안끝난 도시*/ && (totalPay[i]==Integer.MAX_VALUE) /*최대값인 경우*/ && exist[start][i]/*연결되어있는경우*/){
        totalPay[i]=totalPay[start]+cityToCity[start][i];
      }else if(!visitCity[i]&&(totalPay[i]!=Integer.MAX_VALUE)&&(exist[start][i])){
        totalPay[i]=Math.min(totalPay[start]+cityToCity[start][i],totalPay[i]);
      }
    }
    
    int findStart = 100000001;
    int min = Integer.MAX_VALUE;
    
    for(int i=0; i<visitCity.length; i++){
 // System.out.print((totalPay[i])+" ");
      if(!visitCity[i]&&totalPay[i]<min&&(totalPay[i]!=0||exist[start][i])){
        findStart=i;
        min = totalPay[i];
      }
    }
// System.out.println();

    if(findStart!=100000001){
      dijkstra(cityToCity, totalPay, visitCity, findStart);
    }
    
  }
  
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str = br.readLine();
    int N = Integer.parseInt(str); // 도시개수
    str = br.readLine();
    int M = Integer.parseInt(str); // 버스개수
    cityToCity = new int[N][N];
    totalPay = new int[N];
    for(int i=0; i<N; i++){
      totalPay[i]=Integer.MAX_VALUE;
    }
    visitCity = new boolean[N];
    exist = new boolean[N][N];
    for(int i = 0; i<M; i++){
      str = br.readLine();
      String[] inputArray = str.trim().split(" ");
      int city1 = Integer.parseInt(inputArray[0])-1;
      int city2 =Integer.parseInt(inputArray[1])-1;
      int pay = Integer.parseInt(inputArray[2]);
      if(city1==city2){continue;}
      else{
      if(cityToCity[city1][city2]==0&&!exist[city1][city2]){
        exist[city1][city2]=true;
        cityToCity[city1][city2]=pay;
      }else if(cityToCity[city1][city2]==0 && exist[city1][city2]){
        
      } else if(cityToCity[city1][city2]>pay){
        cityToCity[city1][city2]=pay; //비싼표는 싸게
      } 
      }
    }
    // for(int i=0; i<N; i++){
    //   for(int j=0; j<N; j++){
    //     System.out.print((cityToCity[i][j])+" ");
    //   }
    //   System.out.println();
    // }
    str = br.readLine();
    String[] arr = str.trim().split(" ");
    int start = Integer.parseInt(arr[0])-1; //시작점
    int end = Integer.parseInt(arr[1])-1; // 끝점
    totalPay[start]=0;
    dijkstra(cityToCity, totalPay, visitCity, start);
   // System.out.println();
    // for(int i=0; i<N; i++)
    //   System.out.print((totalPay[i])+" ");
    // System.out.println();

    System.out.println(totalPay[end]);
  }
}

//////////////////////////////////////////
/////////////////////////////////////////
////////////////////////6%에러나는데 무슨문제인지 모르겠다 시팔