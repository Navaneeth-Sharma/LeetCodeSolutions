class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int vals =1;
        int length = 0;
        ListNode temp = new ListNode();
        ListNode current = head;
        while(current!=null){
            vals++;length++;
            current = current.next;
        }current = head;
        int required = vals-n;
        vals=1;
        if(length==1){
            head = null;
        }else if(length==2){
            if(n==2){
           head=head.next;}else{
                head.next=null;
            } 
        }else{
        while(current!=null){
          if(required-1==vals){
            temp= current.next;
              current.next = temp.next;break;
}  current = current.next;
            vals++;
        }if(n==length){
            head= head.next;
        }
        }  return head;
    }
}
