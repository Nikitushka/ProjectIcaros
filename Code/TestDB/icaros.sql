--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2 (Ubuntu 13.2-1.pgdg20.04+1)
-- Dumped by pg_dump version 13.2 (Ubuntu 13.2-1.pgdg20.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
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
-- Name: scan; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.scan (
    scan_id integer NOT NULL,
    frequency numeric,
    signal_strenght numeric,
    mod_enc character varying(10),
    ssid character varying(40),
    bssid character varying(40),
    lon numeric NOT NULL,
    lat numeric NOT NULL
);


--
-- Name: scan_scan_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.scan_scan_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: scan_scan_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.scan_scan_id_seq OWNED BY public.scan.scan_id;


--
-- Name: scan scan_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.scan ALTER COLUMN scan_id SET DEFAULT nextval('public.scan_scan_id_seq'::regclass);


--
-- Data for Name: scan; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.scan (scan_id, frequency, signal_strenght, mod_enc, ssid, bssid, lon, lat) FROM stdin;
1	94.0	-21	\N	\N	\N	60.20140429413731	24.933825185203837
2	94.0	-21	\N	\N	\N	60.201	24.933825
3	94.0	-21	\N	\N	\N	60.201	24.933825
4	94.0	-21	\N	\N	\N	60.201	24.933825
5	2.5	-21	WPA2	mutsis	\N	59.201	24.933825
6	\N	\N	WPA3	just_se	\N	59.201	24.933825
\.


--
-- Name: scan_scan_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.scan_scan_id_seq', 7, true);


--
-- Name: scan scan_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.scan
    ADD CONSTRAINT scan_pkey PRIMARY KEY (scan_id);


--
-- PostgreSQL database dump complete
--

