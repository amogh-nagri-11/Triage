--
-- PostgreSQL database dump
--

-- Dumped from database version 17.4
-- Dumped by pg_dump version 17.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: patients; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.patients (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    age integer NOT NULL,
    heart_rate integer,
    blood_pressure integer,
    temperature numeric(4,1),
    chief_complaint_chest_pain boolean DEFAULT false,
    chief_complaint_fever boolean DEFAULT false,
    chief_complaint_headache boolean DEFAULT false,
    chief_complaint_difficulty_breathing boolean DEFAULT false,
    chief_complaint_abdominal_pain boolean DEFAULT false,
    chief_complaint_fracture boolean DEFAULT false,
    chief_complaint_unconscious boolean DEFAULT false,
    chief_complaint_nausea boolean DEFAULT false,
    chief_complaint_stroke_symptoms boolean DEFAULT false,
    chief_complaint_burn_injury boolean DEFAULT false,
    severity character varying(50) DEFAULT 'Unknown'::character varying,
    gender character varying(10) NOT NULL,
    weight numeric(5,2) NOT NULL
);


ALTER TABLE public.patients OWNER TO postgres;

--
-- Name: patients_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.patients_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.patients_id_seq OWNER TO postgres;

--
-- Name: patients_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.patients_id_seq OWNED BY public.patients.id;


--
-- Name: patients id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patients ALTER COLUMN id SET DEFAULT nextval('public.patients_id_seq'::regclass);


--
-- Data for Name: patients; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.patients (id, name, age, heart_rate, blood_pressure, temperature, chief_complaint_chest_pain, chief_complaint_fever, chief_complaint_headache, chief_complaint_difficulty_breathing, chief_complaint_abdominal_pain, chief_complaint_fracture, chief_complaint_unconscious, chief_complaint_nausea, chief_complaint_stroke_symptoms, chief_complaint_burn_injury, severity, gender, weight) FROM stdin;
\.


--
-- Name: patients_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.patients_id_seq', 1, false);


--
-- Name: patients patients_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patients
    ADD CONSTRAINT patients_pkey PRIMARY KEY (id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: pg_database_owner
--

GRANT USAGE ON SCHEMA public TO triage_user;


--
-- Name: TABLE patients; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT ON TABLE public.patients TO triage_user;


--
-- Name: SEQUENCE patients_id_seq; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON SEQUENCE public.patients_id_seq TO triage_user;


--
-- Name: DEFAULT PRIVILEGES FOR TABLES; Type: DEFAULT ACL; Schema: public; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT SELECT ON TABLES TO triage_user;


--
-- PostgreSQL database dump complete
--

