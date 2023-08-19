import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

class Line{
	int x1;
	int x2;
	int y1;
	int y2;
	public Line() {
		// TODO Auto-generated constructor stub
	}
	Line(int x1, int y1, int x2, int y2){
		this.x1=x1;
		this.x2=x2;
		this.y1=y1;
		this.y2=y2;
	}
	
	boolean visit=false;
	List<Line> cross = new LinkedList<>();
}

public class Main {
	static Line[] lines;
	static Set<Line> set = new HashSet<>();
	public static void crossCheck(Line line) {
		line.visit=true;
		set.add(line);
		for(int i=0; i<lines.length; i++) {
			if(!lines[i].visit) {
				if(isCross(line.x1, line.y1, line.x2, line.y2, lines[i].x1, lines[i].y1, lines[i].x2, lines[i].y2)) {
					line.cross.add(lines[i]);
					lines[i].cross.add(line);
					crossCheck(lines[i]);
				}
			}
		}
	}
	
	 static int CCW(long x1, long y1, long x2, long y2, long x3, long y3) {
		    long temp = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3);
		    if(temp > 0) return 1;
		    else if(temp < 0) return -1;
		    return 0;
		}
		 //선분겹침여부 판별 함수
		 private static boolean isOverlab(long x1,long y1,long x2,long y2,long x3,long y3,long x4,long y4){ 
		if(Math.min(x1, x2) <= Math.max(x3, x4) && Math.min(x3, x4) <= Math.max(x1, x2)
		   && Math.min(y1, y2) <= Math.max(y3, y4) && Math.min(y3, y4) <= Math.max(y1, y2))return true;
		   return false;
		  }
		  private static boolean isCross(long x1,long y1,long x2,long y2,long x3,long y3,long x4,long y4) {
		    int abc = CCW(x1, y1, x2, y2, x3, y3);
		    int abd = CCW(x1, y1, x2, y2, x4, y4);
		    int cda = CCW(x3, y3, x4, y4, x1, y1);
		    int cdb = CCW(x3, y3, x4, y4, x2, y2);
		    if(abc * abd == 0 && cda * cdb == 0) {  // 선분이 일직 선인 경우
		      return isOverlab(x1, y1, x2, y2, x3, y3, x4, y4);  //겹치는 선분인지 판별하기
		    }else if(abc * abd <= 0 && cda * cdb <= 0) {  // 선분이 교차하는 경우
		      return true;
		    }
		    return false;
	}
	
	

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		int N = Integer.parseInt(str);
		lines = new Line[N];
		for(int i=0; i<N; i++) {
			str=br.readLine();
			String[] points = str.trim().split(" ");
			lines[i] = new Line(Integer.parseInt(points[0]), 
					Integer.parseInt(points[1]), 
					Integer.parseInt(points[2]), 
					Integer.parseInt(points[3]));	
		}
		int setCount = 0;
		int maxSetSize = 0;
		for(int i=0; i<N; i++) {
			if(!lines[i].visit) {
				crossCheck(lines[i]);
				setCount++;
				maxSetSize = Math.max(maxSetSize, set.size());
				set.clear();
			}
		}
		System.out.println(setCount);
		System.out.println(maxSetSize);
		

	}

}
