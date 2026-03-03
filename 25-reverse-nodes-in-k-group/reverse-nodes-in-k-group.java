
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode curr = head;
        int count = 0;

        while (curr != null && count < k) {
            curr = curr.next;
            count++;
        }


        if (count == k) {

            ListNode prev = null;
            ListNode nextNode = null;
            ListNode tempCurr = head;
            
            for (int i = 0; i < k; i++) {
                nextNode = tempCurr.next;
                tempCurr.next = prev;
                prev = tempCurr;
                tempCurr = nextNode;
            }

            if (nextNode != null) {
                head.next = reverseKGroup(nextNode, k);
            }


            return prev;
        }

    
        return head;
    }
}
