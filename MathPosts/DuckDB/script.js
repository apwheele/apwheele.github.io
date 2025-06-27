document.addEventListener('DOMContentLoaded', async () => {
    const executeButton = document.getElementById('execute-button');
    const sqlQuery = document.getElementById('sql-query');
    const tableContainer = document.getElementById('table-container');
    const statusMessage = document.getElementById('status-message');
    const downloadCsvButton = document.getElementById('download-csv-button');

    const query1Button = document.getElementById('query1-button');
    const query2Button = document.getElementById('query2-button');
    const query3Button = document.getElementById('query3-button');

    let db;
    let currentData = [];
    let sortColumn = null;
    let sortDirection = 'asc';
    let currentPage = 1;
    const rowsPerPage = 10;

    async function init() {
        try {
            const JSDELIVR_BUNDLES = window.duckdb.getJsDelivrBundles();
            const bundle = await window.duckdb.selectBundle(JSDELIVR_BUNDLES);
            const worker = await window.duckdb.createWorker(bundle.mainWorker);
            const logger = new window.duckdb.ConsoleLogger();
            db = new window.duckdb.AsyncDuckDB(logger, worker);
            await db.instantiate(bundle.mainModule, bundle.pthreadWorker);
            executeButton.disabled = false;
            statusMessage.textContent = 'DuckDB is ready. Enter a query and click Execute.';
        } catch (e) {
            statusMessage.textContent = `Error initializing DuckDB: ${e.toString()}`;
            console.error(e);
        }
    }

    await init();

    // Event listeners for pre-defined query buttons
    query1Button.addEventListener('click', () => {
        sqlQuery.value = query1Button.dataset.query;
        executeButton.click();
    });

    query2Button.addEventListener('click', () => {
        sqlQuery.value = query2Button.dataset.query;
        executeButton.click();
    });

    query3Button.addEventListener('click', () => {
        sqlQuery.value = query3Button.dataset.query;
        executeButton.click();
    });

    executeButton.addEventListener('click', async () => {
        const query = sqlQuery.value;
        if (!query) {
            alert('Please enter a SQL query.');
            return;
        }

        try {
            const conn = await db.connect();
            const result = await conn.query(query);
            conn.close();

            if (result.numRows > 0) {
                currentData = result.toArray().map(row => row.toJSON());
                sortColumn = null;
                sortDirection = 'asc';
                currentPage = 1;
                renderTable();
                downloadCsvButton.style.display = 'block'; // Show the download button
            } else {
                tableContainer.innerHTML = '<p>No results found.</p>';
                downloadCsvButton.style.display = 'none'; // Hide the download button
            }
        } catch (error) {
            console.error(error);
            tableContainer.innerHTML = `<p>Error: ${error.message}</p>`;
        }
    });

    function renderTable() {
        tableContainer.innerHTML = ''; // Clear previous table

        if (currentData.length === 0) {
            tableContainer.innerHTML = '<p>No results found.</p>';
            return;
        }

        const columns = Object.keys(currentData[0]);

        // Sort data
        let sortedData = [...currentData];
        if (sortColumn) {
            sortedData.sort((a, b) => {
                const valA = a[sortColumn];
                const valB = b[sortColumn];

                if (valA < valB) return sortDirection === 'asc' ? -1 : 1;
                if (valA > valB) return sortDirection === 'asc' ? 1 : -1;
                return 0;
            });
        }

        // Paginate data
        const totalPages = Math.ceil(sortedData.length / rowsPerPage);
        const startIndex = (currentPage - 1) * rowsPerPage;
        const endIndex = startIndex + rowsPerPage;
        const paginatedData = sortedData.slice(startIndex, endIndex);

        const table = d3.select(tableContainer).append('table').attr('class', 'table table-striped table-hover');
        const thead = table.append('thead');
        const tbody = table.append('tbody');

        // Append the header row
        thead.append('tr')
            .selectAll('th')
            .data(columns)
            .enter()
            .append('th')
            .text(d => d)
            .on('click', (event, column) => {
                if (sortColumn === column) {
                    sortDirection = sortDirection === 'asc' ? 'desc' : 'asc';
                } else {
                    sortColumn = column;
                    sortDirection = 'asc';
                }
                renderTable();
            });

        // Append the data rows
        const rows = tbody.selectAll('tr')
            .data(paginatedData)
            .enter()
            .append('tr');

        rows.selectAll('td')
            .data(row => columns.map(column => row[column]))
            .enter()
            .append('td')
            .text(d => {
                if (typeof d === 'number') {
                    return d3.format(".4~f")(d);
                }
                return d;
            });

        // Pagination controls
        const paginationDiv = d3.select(tableContainer).append('div').attr('class', 'pagination mt-3');

        paginationDiv.append('button')
            .attr('class', 'btn btn-secondary me-2')
            .attr('disabled', currentPage === 1 ? true : null)
            .text('Previous')
            .on('click', () => {
                currentPage--;
                renderTable();
            });

        paginationDiv.append('span').text(`Page ${currentPage} of ${totalPages}`);

        paginationDiv.append('button')
            .attr('class', 'btn btn-secondary ms-2')
            .attr('disabled', currentPage === totalPages ? true : null)
            .text('Next')
            .on('click', () => {
                currentPage++;
                renderTable();
            });
    }

    downloadCsvButton.addEventListener('click', () => {
        if (currentData.length === 0) {
            alert('No data to download.');
            return;
        }

        const columns = Object.keys(currentData[0]);
        let csvContent = columns.join(',') + '\n';

        currentData.forEach(row => {
            const rowValues = columns.map(col => {
                let value = row[col];
                if (typeof value === 'string' && value.includes(',')) {
                    value = `"${value.replace(/"/g, '""')}"`; // Enclose in double quotes and escape existing double quotes
                }
                return value;
            });
            csvContent += rowValues.join(',') + '\n';
        });

        const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
        const link = document.createElement('a');
        if (link.download !== undefined) { // Feature detection for download attribute
            const url = URL.createObjectURL(blob);
            link.setAttribute('href', url);
            link.setAttribute('download', 'query_results.csv');
            link.style.visibility = 'hidden';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            URL.revokeObjectURL(url);
        } else {
            alert('Your browser does not support downloading files directly. Please copy the data manually.');
        }
    });
});