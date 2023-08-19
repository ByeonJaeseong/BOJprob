import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		List<Long> list = new ArrayList<Long>();
		int count = 0;
		
		for(int i=0; i<N; i++) {
			list.add(sc.nextLong());
		}
		list.sort(null);
		for(int i=0; i<N; i++) {
			Long p = list.get(i);
			int q = 0;
			int r = N-1;
			//System.out.println((i)+"에 대한 실행입니다.");
			while(q<r) {
			if(list.get(q)+list.get(r)<p) {
				q++;
		//		System.out.println("q를 증가시킵니다.");
			}else if(list.get(q)+list.get(r)>p) {
				r--;
			//	System.out.println("r을 감소시킵니다.");
			}else {
			
				if(q!=i&&r!=i) {
					//System.out.println((q)+":"+(list.get(q))+" "+" "+(r)+":"+(list.get(r)));
					count++;
					break;
				} else if(q==i) {
					q++;
					//System.out.println("q와 i가 같습니다.");
				} else if(r==i) {
					r--;
					//System.out.println("r과 i가 같습니다.");
				}

			}
			}
		}
		
		System.out.print(count);

	}

}