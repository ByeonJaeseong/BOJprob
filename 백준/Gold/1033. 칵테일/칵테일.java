import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

class Ingre{
  int Num = 0;
  int n=1;
  boolean visit;
  Ingre(){};
  Ingre(int Num){
    this.Num=Num;
  }
  ArrayList<Ingre> adj = new ArrayList<Ingre>();
  
}

class Main {
  public static void update(Ingre ingre, int x, int y){
    ingre.visit=true;
    ingre.n*=x;
    ingre.n*=y;
    for(int i=0; i<ingre.adj.size(); i++){
      if(!ingre.adj.get(i).visit){        
        update(ingre.adj.get(i), x, y);        
      }
    }
    ingre.visit=false;
  }

  public static int[] gcd(int[] recipe){
    int N = recipe.length;
    int[] div = {2, 3, 5, 7};
    for(int i=0; i<4; i++){
     
      while(true){
       int mark =0;
       for(int j=0; j<N; j++){
         if(recipe[j]%div[i]==0){
           mark++;
         }else{
           break;
         }
       }
   //     System.out.println(mark);
       if(mark==N){
         for(int j=0; j<N; j++){
           recipe[j]/=div[i];
         }
      //   System.out.println((div[i])+"실행");
       }else{
         break;
       }
     } 
      
    }

    return recipe;
      
  }  
  
  public static void main(String[] args) throws Exception {
    //아이디어 탐색할때마다 상대방의 입력값을 반대쪽에 곱함
    //그리고 비율을 전체 연결된 수에 곱해나감
    
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str = br.readLine();
    int N = Integer.parseInt(str);
    String[] inputNo;
    Ingre[] ingres = new Ingre[N];
    int[] recipe = new int[N];
    for(int i=0; i<N; i++){
      ingres[i] = new Ingre(i);
    }

    for(int i=0; i<N-1; i++){
      str =br.readLine();
      inputNo = str.trim().split(" ");
      int n = Integer.parseInt(inputNo[0]);
      int m = Integer.parseInt(inputNo[1]);
      int x = Integer.parseInt(inputNo[2]);
      int y = Integer.parseInt(inputNo[3]);
      int p = ingres[n].n;
      int q = ingres[m].n;
      // ingres[n].n*=q;
      // ingres[m].n*=p;
      update(ingres[n], x, q);
      update(ingres[m], y, p);
      ingres[n].adj.add(ingres[m]);
      ingres[m].adj.add(ingres[n]);
      
    }

    for(int i=0; i<N; i++){
      recipe[i] = ingres[i].n;
   //   System.out.print((recipe[i])+" ");
    
    }
    gcd(recipe);
    for(int i=0; i<N; i++){
      if(i!=N-1)
        System.out.print((recipe[i])+" ");
      else
        System.out.print(recipe[i]);
    
    }

    
  }
}