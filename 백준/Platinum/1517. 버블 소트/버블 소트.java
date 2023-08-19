import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	public static int[] A, tmp;
	public static long result=0;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		int N = Integer.parseInt(str);
		str = br.readLine();
		String[] strNo = str.trim().split(" ");//trim->앞뒤 공백제거
		A = new int[N+1];
		tmp = new int[N+1];
		for(int i=1; i<=N; i++) {
			A[i]=Integer.parseInt(strNo[i-1]);		
		}
		merget_sort(1, N);
		System.out.print(result);
	}	
	
	//앞에 자기 자신보다 큰 수의 개수의 합 -> 정답
	//뒤에 자기 자신보다 작은 수의 개수의 합 -> 정답
		
	private static void merget_sort(int s, int e) {
	    if (e - s < 1)
		      return;
	    int m = s + (e - s) / 2;
	    // 재귀함수 형태로 구현
	    merget_sort(s, m);
	    merget_sort(m + 1, e);
	    for (int i = s; i <= e; i++) {
	     tmp[i] = A[i];
	    }
	    int k = s;
	    int index1 = s;//end m
	    int index2 = m + 1;
	    while (index1 <= m && index2 <= e) { // 두 그룹을 Merge 해주는 로직
	      if (tmp[index1] > tmp[index2]) {
	        A[k] = tmp[index2];
	        k++;
	        index2++;
	        result=result+m-index1+1;
	       // System.out.println(result);
	      } else {
	        A[k] = tmp[index1];
	        k++;
	        index1++;
	        
	      }
	    }
	    // 한쪽 그룹이 모두 선택된 후 남아있는 값 정리하기
	    while (index1 <= m) {
	      A[k] = tmp[index1];
	      k++;
	      index1++;
	    }
	    while (index2 <= e) {
	      A[k] = tmp[index2];
	      k++;
	      index2++;
	    }
	}
}

