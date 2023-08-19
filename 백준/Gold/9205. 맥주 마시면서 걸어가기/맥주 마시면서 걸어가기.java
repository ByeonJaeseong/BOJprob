
/*
2 /test case
2 /convenience store
0 0 / 상근이네 집
1000 0 / 편의점
1000 1000 / 편의점
2000 1000 / 펜타포트락페스티벌
2
0 0
1000 0
2000 1000
2000 2000
*/
import java.io.*;
import java.util.*;

class cStore {
  int x;
  int y;
  boolean visit = false;

  cStore(int x, int y) {
    this.x = x;
    this.y = y;
  }
}

class Main {

  public static cStore[] cStores;
  public static boolean result;
  public static int xResult;
  public static int yResult;

  public static void bfs(cStore store) {
    store.visit = true;
    if (Math.abs(store.x - xResult) + Math.abs(store.y - yResult) <= 1000) {
      result = true;
    } else {
      Queue<cStore> queue = new LinkedList<cStore>();
      for (int i = 0; i < cStores.length; i++)
        if ((Math.abs(store.x - cStores[i].x) + Math.abs(store.y - cStores[i].y) <= 1000)
            && (store.x != cStores[i].x || store.y != cStores[i].y)
            && !cStores[i].visit) {
          queue.add(cStores[i]);
        }
      while (!queue.isEmpty()) {
        cStore store2 = queue.poll();
        bfs(store2);
      }


    }
  }

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str = br.readLine();
    int N = Integer.parseInt(str); // test 횟수

    for (int r = 0; r < N; r++) {
      result = false;
      str = br.readLine();
      String[] loc = str.trim().split(" ");
      int M = Integer.parseInt(str); // 편의점 갯수
      str = br.readLine();
      loc = str.trim().split(" ");
      int x = Integer.parseInt(loc[0]);
      int y = Integer.parseInt(loc[1]);
      cStore house = new cStore(x, y);
      cStores = new cStore[M];
      for (int i = 0; i < M; i++) {
        str = br.readLine();
        loc = str.trim().split(" ");
        x = Integer.parseInt(loc[0]);
        y = Integer.parseInt(loc[1]);
        cStores[i] = new cStore(x, y);
      }
      str = br.readLine();
      loc = str.trim().split(" ");
      xResult = Integer.parseInt(loc[0]);
      yResult = Integer.parseInt(loc[1]);
      bfs(house);
      if (result) {
        System.out.println("happy");
      } else {
        System.out.println("sad");
      }

    }

  }
}