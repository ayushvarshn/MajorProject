for row = [1:46]
    filename = 'CH'+string(batch(row).channel_id)+'.csv';
    csv(1, :) = ["cycle", "time", "charge", "current", "voltage", "temp", "discharge", "soc"];
    no_of_cycles = size(batch(row).cycles, 2);
    for i = [2:no_of_cycles]
        no_of_indices = size(batch(row).cycles(i).t, 1);
        sz_prev = size(csv, 1);
        csv(sz_prev +1 : sz_prev + no_of_indices, : ) = [i*ones(no_of_indices, 1), batch(row).cycles(i).t, batch(row).cycles(i).Qc, batch(row).cycles(i).I, batch(row).cycles(i).V, batch(row).cycles(i).T, batch(row).cycles(i).Qd, max((batch(row).cycles(i).Qc-batch(row).cycles(i).Qd)*100/1.1, 0)];
    end
    writematrix(csv, filename)
    clear csv
    clear sz_prev
    clear no_of_cycles
    clear no_of_indices
    clear i
    clear filename
end