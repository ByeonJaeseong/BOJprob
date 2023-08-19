import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class feed implements Comparable<feed> {
  String feedName;
  int first = 0;
  boolean end = false;

  feed() {
  }

  feed(String feedName) {
    this.feedName = feedName;
  }

  ArrayList<feed> underFeed = new ArrayList<feed>();

  @Override
  public int compareTo(feed f) {
    return feedName.compareTo(f.feedName);
  }
}

class Main {

  public static void fPrint(feed fFeed) {
    Collections.sort(fFeed.underFeed);
    for (int i = 0; i < fFeed.first; i++) {
      System.out.print("--");
    }
    System.out.println(fFeed.feedName);
    for (int i = 0; i < fFeed.underFeed.size(); i++) {
      fPrint(fFeed.underFeed.get(i));
    }

  }

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str = br.readLine();
    String[] input;
    int N = Integer.parseInt(str);
    ArrayList<feed> feeds = new ArrayList<feed>();
    for (int i = 0; i < N; i++) {
      str = br.readLine();
      input = str.trim().split(" ");
      int M = Integer.parseInt(input[0]);
      int x = Integer.MAX_VALUE;
      for (int j = 0; j < feeds.size(); j++) {
        if (feeds.get(j).feedName.equals(input[1])) {
          x = j;
        }
      }
      if (x == Integer.MAX_VALUE) {
        feeds.add(new feed(input[1]));
        x = feeds.size() - 1;
      }

      feed fFeed = feeds.get(x);

      for (int j = 2; j <= M; j++) {
        x = Integer.MAX_VALUE;

        for (int k = 0; k < fFeed.underFeed.size(); k++) {
          if (fFeed.underFeed.get(k).feedName.equals(input[j])) {
            x = k;
          }
        }

        if (x == Integer.MAX_VALUE) {
          fFeed.underFeed.add(new feed(input[j]));
          x = fFeed.underFeed.size() - 1;
        } // x값에 데이터 입력

        fFeed = fFeed.underFeed.get(x);

        fFeed.first = j - 1;
        if (j == M) {
          fFeed.end = true;
        } else {
          fFeed.end = false;
        }

      }

    }
    Collections.sort(feeds);

    for (int i = 0; i < feeds.size(); i++) {
      fPrint(feeds.get(i));
    }

  }
}