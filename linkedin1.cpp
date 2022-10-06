int lastStoneWeight(vector<int> &weights)
{
    priority_queue<int> pq(begin(weights), end(weights));
    while (pq.size() > 1)
    {
        int x = pq.top();
        pq.pop();
        int y = pq.top();
        pq.pop();
        if (x > y)
            pq.push(x - y);
    }
    return pq.empty() ? 0 : pq.top();
}