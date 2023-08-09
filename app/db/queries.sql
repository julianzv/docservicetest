---postgresql

create table if not exists document_job (
    id uuid primary key,
    time_stamp timestamp not null,
    document_status varchar(20) not null,
    event_type varchar(20) not null,
    document_data jsonb not null
);

create table if not exists document (
    id uuid primary key,
    created_at timestamp not null,
    modified_at timestamp not null,
    path_to_file varchar(255) not null,
    policy_status varchar(20) not null,
    policy_id uuid not null,
    account_id uuid not null,
    company_id uuid not null,
    product_id uuid not null,
    document_job_id uuid not null,
    foreign key (document_job_id) references document_job(id)
);

